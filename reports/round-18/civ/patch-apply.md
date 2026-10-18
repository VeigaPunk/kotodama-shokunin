# Round-18 C patch-apply receipt — civ-map revision (R18-C01/C02)

- Seat: CIV R18-C01/C02 (map revision: apply the round-17 map patch; re-verify the
  5 attempt-documented rows).
- Claim: C / coverage (`reports/round-18/claims.json`, claim `C`; counting command
  `python3 reports/round-18/run-validation.py`).
- Date: 2026-10-18. Baseline `3dd3754207032cb81f5fb3e202fe85cf79211339`; HEAD at build
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`.
- Deliverables:
  - `reports/round-18/civ-map-r18.json` — sha256
    `5fb4dd1cb948abbbbdb7b3182e5ba47cb15057da3519bd8bc63ad022ad8bf796` (new revision file;
    94 rows; 12 transitions applied; 82 rows carried verbatim).
  - this receipt.
- Status: patch applied to a new revision; 12/12 rows re-verified live today; gate
  (round-16 validator's own civ-map checks) re-run green on the new revision; the
  round-16 map is byte-unchanged. NON-CANON: locator/status receipts only, no
  canon, rights, clearance or freshness-axis verdict.

## §0 Identity chain (bytes before anything was written)

```
sha256sum reports/round-17/civ/map-patch.json reports/round-16/civ-map.json
79ceafabac9fd84d6bec5cb701e3d1791b075e5e1300d7164126e40f9876e77e  reports/round-17/civ/map-patch.json
07cabb69b4a41c51b74767212a07ba4ffae3c09ef8c2571abd954b37342cb943  reports/round-16/civ-map.json
```
Run 2026-10-18. The round-16 map hash equals the patch's `target.sha256`
(`reports/round-17/civ/map-patch.json:8`) — the patch's `from_` values bind to the filed
round-16 row bytes, and the patch was built against these exact bytes.

Corpus partition at build (`ls corpus/knowledge/civilizations/*.md | wc -l` → `94`,
2026-10-18) equals the round-16 map's `count`/`complete` declaration
(`reports/round-16/civ-map.json`), so the new revision keeps the same 94-entry universe.

## §1 Preconditions asserted at apply time

Run inside the scratch builder (`python3 .scratch/r18c01/build-map.py`, 2026-10-18):

1. `sha256(reports/round-16/civ-map.json) == patch.target.sha256` — asserted; refused to
   proceed on drift.
2. For each of the 12 patch rows: every key of `from_` byte-equals the filed round-16 row
   for the same `file` (with `from_.evidence_path: null` read as "the filed row has no
   `evidence_path` key"). All 12 asserted (`applied_patch.from_rows_asserted_equal_to_
   round16_map` in the revision). Dispatch also asserted `idx_round16_1based` matches the
   row's 1-based position in the round-16 `entries` array.
3. For each of the 12 files: `sha256(corpus/knowledge/civilizations/<file>)` equals the
   patch's `disposition.sha256_after` — 12/12 hold today (command and output below), so the
   round-17 deliverables are still exactly the bytes the patch binds to.

```
python3 - <<'EOF'
import hashlib, json, pathlib
patch=json.load(open('reports/round-17/civ/map-patch.json'))
civ=pathlib.Path('corpus/knowledge/civilizations')
for r in patch['rows']:
    h=hashlib.sha256((civ/r['file']).read_bytes()).hexdigest()
    print(f"{r['file']:34} {h[:16]} {r['disposition']['sha256_after'][:16]} {h==r['disposition']['sha256_after']}")
EOF
```
→ 12/12 `True` (2026-10-18; full run recorded in §3's `after` column).

**Defect found by the gate and fixed before filing** (recorded because it was a real
near-miss): the first build wrote the patch's `to` objects as the new rows, but `to` does
not carry the `file` key (the patch keeps `file` at patch-row level). The round-16
validator's `row_entry()` returned `''` for those 12 rows: `passed: False`,
`civ-map row #43 names no civilization entry` (… rows 43, 60, 61, 66, 67, 76–82 …),
`map 82 rows vs 94 corpus entries`. Fixed by building the row as `{"file": name, **to}` and
re-running; the filed revision is the fixed build.

## §2 Apply procedure (reproducible)

- Apply command: `python3 .scratch/r18c01/build-map.py` (round-18 scratch builder; it reads
  the filed round-16 map and the round-17 patch read-only, asserts §1, replaces the 12 rows
  with the patch `to` rows, carries the other 82 rows verbatim, and writes
  `reports/round-18/civ-map-r18.json`). The builder is scratch (`.scratch/` is git-ignored);
  the assertions it makes are re-runnable as the one-liner below, which is also carried in
  every transitioned row's `transition.verify_command`.
- Verification command (prints `True` iff, for all 12 patch rows, the entry bytes still
  hash to `sha256_after` **and** the new revision's row is byte-equal to the patch `to`
  row):

```
python3 -c "import json,hashlib; p=json.load(open('reports/round-17/civ/map-patch.json')); m=json.load(open('reports/round-18/civ-map-r18.json')); r={e['file']:e for e in m['entries']}; print(all(hashlib.sha256(open('corpus/knowledge/civilizations/'+x['file'],'rb').read()).hexdigest()==x['disposition']['sha256_after'] and all(r[x['file']].get(k)==v for k,v in x['to'].items()) for x in p['rows']))"
True
```

Per-row annotations added on top of the patch rows (the patch's own fields stay verbatim):

- `reason_round16` — the round-16 `reason` text carried next to the new `reason`, so the
  round-8/9/16 reason trail stays readable in the map itself (the round-17 receipts also
  kept it in the entries' verified-at lines).
- `verified_r18` — a dated command string (2026-10-18 + the probe command), so every
  transitioned row's new status carries both a date and a command in row text, not only in
  nested blocks.
- `attempt_row` — `true` for the 5 fixed-type rows, `false` for the 7 never-swept rows.
- `transition` — the transition ledger: `patch_row`, `idx_round16_1based`,
  `from_status`, `to_status`, `terminal_status`, `applied_date`, `applied_command`,
  `verify_command`, `fix_receipt` (+ sha256), `fix_verification` (the seat that filed the
  row verdict), `disposition_kind`, `entry_edit`, `entry_sha256_before/after`, `group`,
  `sweep` (never-swept rows), and `r18_recheck` (this seat's probes, §4–§5).

## §3 The 12 transitions (date + command per row)

`from` is the filed round-16 row status (asserted); `to` is the patch's proposed status,
applied verbatim; all 12 rows carry `verified_at: 2026-10-18` and a `command` (patch
`to.command`, quoted below), plus `verified_r18` (this seat's 2026-10-18 probe command).
`after` = sha256 of the entry bytes today = the patch's `sha256_after`.

| # | file | idx | from → to | group | fix receipt (sha256-16) | disposition | edit | after (sha256-16) |
|---|------|-----|-----------|-------|-------------------------|-------------|------|-------------------|
| 1 | inuit.md | 44 | stale-documented → stale-fixed | fixed-type | reports/round-17/civ/inuit.md (7241e6b48f1b3cb5) | locator-replacement | 3 lines | 52c5a11b7b7db949 |
| 2 | maya-classic.md | 61 | stale-documented → stale-fixed | fixed-type | reports/round-17/civ/maya-classic.md (535f47f4e8b3d1b8) | couples-gap-repair | 13/3 | d9608d842ccb97da |
| 3 | mesoamerica-primary-sources.md | 62 | stale-documented → stale-fixed | fixed-type | reports/round-17/civ/mesoamerica.md (e4e546ab461c071e) | locator-replacement + pin re-base | 6/6 | d04d8913e7049615 |
| 4 | mongol.md | 67 | stale-documented → stale-fixed | fixed-type | reports/round-17/civ/mongol.md (47ba5951db3662fa) | debt-retired (no replacement) | 1/1 | e60b3903402034bc |
| 5 | muisca.md | 68 | stale-documented → stale-fixed | fixed-type | reports/round-17/civ/muisca.md (c671d29b041e80fa) | debt-retired (no replacement) | 2/2 | 417b7086b5b3e827 |
| 6 | persia-sasanian.md | 77 | stale-documented → stale-fixed | never-swept | reports/round-17/civ/persia-sasanian.md (1d536dcecbeba301) | sweep + 1 replacement + 1 archive fallback | 4 lines | 20e7513e1f3b288e |
| 7 | polynesia-navigation.md | 78 | stale-documented → stale-fixed | never-swept | reports/round-17/civ/polynesia-navigation.md (02deda5b91dfc92d) | sweep + 9 moved-locator re-pins | 3/3 | a47639dc0774bd7c |
| 8 | rapa-nui.md | 79 | stale-documented → stale-fixed | never-swept | reports/round-17/civ/rapa-nui.md (f58f8af47f9ceaae) | sweep (no replacement) | 1/1 | c893805a82ed953c |
| 9 | rome.md | 80 | stale-documented → **current** | never-swept | reports/round-17/civ/sed77.md (4b628f58991d6916) | sweep (no replacement) | 1/1 | 0b29e05c44f0a55e |
| 10 | ryukyu.md | 81 | stale-documented → stale-fixed | never-swept | reports/round-17/civ/sed78.md (ebf283ffd73f97cf) | sweep (no replacement) | 1/1 | 424fcbb5de9f4d22 |
| 11 | scythian-saka.md | 82 | stale-documented → stale-fixed | never-swept | reports/round-17/civ/sed79.md (d5c3517d126dbe30) | sweep + 1 permanent-301 re-pin | 2/2 | cb3a6428c4b174a4 |
| 12 | siam-thai.md | 83 | stale-documented → stale-fixed | never-swept | reports/round-17/civ/sed80.md (d4f1bd00045510a8) | sweep + 2 canonical 301 re-pins | 4/4 | 8bef2a5b3936c2f4 |

Row `command` values (patch `to.command`, verbatim in the map):

1. inuit — `locator repair + live probe per receipt (curl pageplace preview 206/200, sha256 of fetched PDF)`
2. maya-classic — `couples-gap repair (sacbeob target added) + live source checks per receipt`
3. mesoamerica-primary-sources — `hard-fail URL dispositions + pin re-base per receipt`
4. mongol — `live re-attempt per receipt: curl -L --max-time 30 x4 samples + body content checks`
5. muisca — `live re-attempt per receipt: curl http:// x3 samples + anchor greps on fetched bodies`
6. persia-sasanian — `curl -sS -o /dev/null -w '%{http_code}' -L --max-time 15 -A kotodama-metadata-audit/1.0 (M04 method; 9/9 distinct URLs; retry once on 000) per receipt`
7. polynesia-navigation — `curl -sS -o /dev/null -w '%{http_code}' -L --max-time 15 -A kotodama-metadata-audit/1.0 (M04 method; 26/26 distinct URLs; retry once on 000) per receipt`
8. rapa-nui — `curl -sS -o /dev/null -w '%{http_code}' -L --max-time 20 -A kotodama-metadata-audit/1.0 (M04 method; 9/9 distinct URLs; 2 runs) per receipt`
9. rome — `curl -sS -L --max-time 25 --compressed -A kotodama-metadata-audit/1.0 (M04 method; 12/12 distinct URLs, balanced-paren extraction) per receipt`
10. ryukyu — `curl -sSL --max-time 30 -A <lane UA> -w '%{http_code}' (12/12 distinct URLs, xargs -P 8) per receipt`
11. scythian-saka — `curl -sS -o body -w '%{http_code}' -L --max-time 15 (M04 method; 12/12 distinct URLs, retry on 000) per receipt`
12. siam-thai — `curl -sIL HEAD w/ GET fallback + content probes (curl GET + sed -n '80p'; pdftotext) per receipt`

For rows 2 and 3 the patch's own `command` text names no shell command token (it names the
repair class and points at the receipt); those rows carry this seat's dated command string
in `verified_r18` so the "date+command" requirement holds in row text for every
transitioned row (`transition.r18_recheck.command` carries the exact probe list). Recorded,
not patched over: the patch's `command` values are applied verbatim.

Stale-count movement: `stale-documented` 12 → 0; `current` 82 → 83; `stale-fixed` 0 → 11.
Counting command unchanged and reproducing: `ls corpus/knowledge/civilizations/*.md | wc -l`
→ `94` (2026-10-18).

## §4 Re-verification of the 5 attempt-documented rows (this seat, 2026-10-18)

Probe command (all rows; each URL one request, `curl 8.x`, UA
`kotodama-metadata-audit/1.0`):

```
curl -sS -o /dev/null -w '%{http_code} %{size_download}' -L --max-time 25 \
  -A kotodama-metadata-audit/1.0 <url>
```
Run window 2026-10-18 10:21–10:26 UTC from this lane.

| row | probe | result | against the receipt |
|-----|-------|--------|---------------------|
| inuit | new locator `https://api.pageplace.de/preview/DT0400.9780773581623_A23657095/preview-9780773581623_A23657095.pdf` | **200, 515 139 B**, body sha256 `61388588ca884f514c3e29510fc4ba21cb3d14d0b849e2a728eb87502f5f660d` | byte count equals the patch's 515139; **body digest equals the patch's recorded digest exactly** (`map-patch.json` row 1 `disposition.replacements[0].evidence`) |
| inuit | replaced old locator `https://library.law.utoronto.ca/sites/default/files/toc/Language%20of%20the%20Inuit%20-%20Dorais%20-%202010.pdf` | **404, 95 720 B** | still dead; the replacement remains necessary |
| maya-classic | `https://en.wikipedia.org/wiki/Sacbe` | **200, 178 576 B**, body sha16 `94b6bdafaae439cc` | equals the receipt's recorded sha16 `94b6bdaf` (round-10 sweep copy) — the couples repair's carried source is live and unchanged |
| maya-classic | in-repo: `grep -c sacbeob corpus/knowledge/civilizations/maya-classic.md` | **8** | round-16 C06 reproduction was 0 hits; the `transport-mobility-lexicon.md:20` couples pointer now resolves in-entry. NOT re-probed: the `mesoweb.com` handbook PDF (49.9 MB, digest in the receipt unchanged) |
| mesoamerica | replacement locator `https://scholarworks.iu.edu/journals/index.php/bookman/article/view/3788` | **200, 19 081 B** | equals the receipt byte count; the rotted `liblilly.sitehost.iu.edu` URL's replacement is live |
| mesoamerica | retained-with-caveat `https://florentinecodex.getty.edu/en/book/12/folio/19v` | **000** strict / **200, 267 502 B** with `-k` | the incomplete-TLS-chain caveat reproduces; byte count equals the receipt's 267502 |
| mongol | `https://depts.washington.edu/silkroad/texts/rubruck.html` | **200, 289 660 B** | equals the receipt byte count; the round-8 hard-fail 000 does not reproduce |
| muisca | `http://muysca.cubun.org/{nyia,chunso,chyquy,psihipqua}` | **200** ×4 (30 692 / 25 827 / 33 028 / 32 263 B) | all four live; http-only host (https 000), locator strings unchanged |

Result line: all five attempt rows re-verified; no new defect found; every probe is recorded
per row in `entries[].transition.r18_recheck`.

## §5 Sampled re-verification of the 7 never-swept rows (same window)

One named locator per row (the replacement/301 target or the recorded bot wall):

| row | probe | result |
|-----|-------|--------|
| persia-sasanian | SR14 replacement PDF `…/Compareti_SR14_2016_71_83.pdf` | 200, 948 943 B, `application/pdf` — equals receipt |
| persia-sasanian | Wayback fallback for `avesta.org/mp/grb.htm` | 200, 127 638 B — receipt said 127643 B, the verifier 127635 B; Wayback re-renders (±5–8 B), content class same |
| polynesia-navigation | `https://pollex.org.nz/entry/moana/` | 200, 31 663 B |
| polynesia-navigation | `https://wehe.hilo.hawaii.edu/?q=k%C4%81pe%CA%BBa` | 200, 117 921 B |
| rapa-nui | `https://www.metmuseum.org/essays/easter-island` (and `/art/collection/search/312238`) | 429 / 429 — the host-wide bot wall reproduces |
| rome | `https://numismatics.org/ocre/id/ric.1(2).aug.206` | 200, 80 524 B — live with balanced-paren extraction (the receipt's 11 046 is the compressed wire column; the patch's `limits` say so) |
| ryukyu | `https://www.mdpi.com/2077-1444/10/5/298` | 403, 398 B — MDPI bot wall reproduces |
| scythian-saka | `https://scholarlypublications.universiteitleiden.nl/handle/1887/16379` | 200, 8 911 B — equals receipt |
| siam-thai | `https://theculturalatlas.org/thai-culture/thai-culture-naming` and the cdlib Ramayana book page | 200, 118 615 B / 200, 1 657 019 B — both equal receipt |

No divergence that changes any row's status; the two byte-level notes (Wayback render
variance, rome's compressed-bytes column) are recorded in the affected rows'
`transition.r18_recheck`.

## §6 Label policy (the patch explicitly delegates this)

The patch (`label_policy_note`) files 11 `stale-fixed` + 1 `current` and permits the
map-scribe to normalize the 11 to `current`. Decision, recorded in the map's
`label_policy` block: **apply the patch's labels verbatim** and carry the terminal reading
explicitly per row (`transition.terminal_status: "current"`) plus
`terminal_status_counts: {current: 94, stale-documented: 0}`. Rationale: "apply the patch"
is the claim's verb; the transition label stays legible in the `status` column; the
terminal reading (the round-16 map's own `current` definition — "cited source re-fetched or
verified in-repo this round, with date+command" — is satisfied by every patched row's
receipt) is recorded beside it. Claim C's counts hold under either labeling
(`stale-documented` 12 → 0).

## §7 Gate evidence on the new revision

1. The round-16 validator's own civ-map checks, re-run against the new revision (global
   rebinding, no filed bytes touched):

```
python3 -c "import importlib.util; s=importlib.util.spec_from_file_location('v','reports/round-16/run-validation.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); m.ROUND_DIR='reports/round-18'; m.CIV_MAP='reports/round-18/civ-map-r18.json'; m.COMMAND='python3 reports/round-18/run-validation.py'; e=m.Evidence(); r=m.measure_c(e); print('passed:', r['passed']); print('failures:', r['failures']); print({k:v['value'] for k,v in r['measurement']['status_histogram'].items()})"
passed: True
failures: []
{'current': 83, 'stale-fixed': 11, 'stale-documented': 0}
```
   (Run 2026-10-18. This exercises the row-set == corpus-partition check, status
   vocabulary, evidence-path resolution + shard pin match, and the status-requirement
   checks — all green, `zero_unstatused: 1`.)
2. Claim-C specifics (scratch checker `.scratch/r18c01/check-map.py`, 2026-10-18), all PASS:
   round-16 map bytes untouched; `count` == corpus 94; counting command → `94`;
   `stale-documented` rows == 0; all 12 patched rows byte-equal the patch `to` rows; every
   transitioned row carries date+command in row text; fix-evidence pointers resolve; 12/12
   entries hash to `sha256_after`; 82 carried rows identical to their round-16 rows; row
   set unchanged (94); every `evidence_path` resolves.

## §8 Non-destruction / append-only

```
git status --porcelain -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 \
  reports/round-12 reports/round-13 reports/round-14 reports/round-15 reports/round-16 reports/round-17 | wc -l
0                      # (2026-10-18) no filed round-8…17 artifact modified
git status --porcelain -- corpus/knowledge/civilizations | wc -l
0                      # the 12 entries are clean; the round-17 edits are committed in 3dd3754
sha256sum reports/round-16/civ-map.json
07cabb69b4a41c51b74767212a07ba4ffae3c09ef8c2571abd954b37342cb943   — unchanged before and after the apply
sha256sum reports/round-18/civ-map-r18.json
5fb4dd1cb948abbbbdb7b3182e5ba47cb15057da3519bd8bc63ad022ad8bf796   — the filed revision
```
The new revision is a new file; the round-16 map and the round-17 receipts are read-only
inputs. The 12 row replacements are re-pins (new rows in a new revision), not in-place edits
of filed bytes. Round-17 receipt hashes are recorded in `evidence_pins`.

## §9 Limits and boundary notes

- Point-in-time: all probes ran 2026-10-18 10:21–10:26 UTC in a 64-worker wave; a single-day
  probe cannot rule out intermittent failure. Bot walls (403/429) and incomplete-TLS-chain
  hosts were re-observed, not worked around.
- Byte counts are wire/identity sizes from `curl -w '%{size_download}'`; for rome the
  receipt's column is the compressed wire size (bigger identity count here by construction),
  and the Wayback fallback byte count varies by a few bytes between renders.
- The 82 carried rows keep their round-16 receipts verbatim (`reports/round-16/civ/*.md`);
  they were not re-audited here — their shard pins are carried in the map's `shards` block
  and still match.
- Gate-integrity note for the round-18 runner seat (evidence, not a defect of this map):
  the round-16 helper `civ_auditors()` excludes the map by *name*
  (`EXCLUDE_NAMES = {… "civ-map.json"}`) and its path exclusion compares
  `path.as_posix()` (absolute) against the relative `CIV_MAP`, so it never fires. With the
  round-18 revision named `civ-map-r18.json`, a straight reuse of that helper counts this
  map itself as an "auditor artifact" (observed: `civ_auditors` → `['reports/round-18/
  civ-map-r18.json']`; dated and command-carrying, it passes the leg). Worth adding
  `civ-map-r18.json` to `EXCLUDE_NAMES` in `reports/round-18/run-validation.py` so the
  auditor requirement is not satisfied by the map it audits; this seat did not write that
  file.
- No canon/rights/clearance/freshness verdict; entry content was not re-read in full — this
  is a status/locator receipt.
