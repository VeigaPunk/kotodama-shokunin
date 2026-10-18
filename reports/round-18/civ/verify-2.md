# R18-C04 — independent verification of the round-17 civ patch, group 2 of 4 (fixed-type B + attempt documentation)

- Verifier seat: **C R18-C04**. This file covers the **fixed-type group B** rows of
  `reports/round-17/civ/map-patch.json` — **`mongol`, `muisca`** — plus the two
  cross-cutting duties of the assignment: the **5 attempt rows' documentation check**
  and the **counting-command reproduction (94)**. Sibling seats: `verify-1.md`
  (C03: `inuit`, `maya-classic`, `mesoamerica-primary-sources`), `verify-3.md`
  (C05: `persia-sasanian`, `polynesia-navigation`, `rapa-nui`, `rome`),
  `verify-4.md` (C06: `ryukyu`, `scythian-saka`, `siam-thai` + 12-row roll-up).
- Date: 2026-10-18; measurement window **10:19–10:33Z** (UTC). Lane HEAD `c66ac3c`;
  pre-fix baseline `f30b6f8` (round-16 close); the fixes landed in `3dd3754`.
- Assignment (verbatim, task brief): *"C R18-C03..C06 (verify x4): independently re-run
  each transitioned row's new evidence (fetch the replacement URLs, spot-check); verify
  the 5 attempt rows' documentation; counting command reproduces 94;
  reports/round-18/civ/verify-{1..4}.md."*
- **NON-CANON.** "Verified" = the fixer's dated, command-carried claims reproduce on
  this seat's independent re-run. No scholarship, freshness, rights or canon verdict.

## 0. Method

Same protocol as `verify-1.md` §0 (read claims → re-fetch independently → hash on disk
→ re-sweep the whole entry → diff against filed git bytes, not receipts). New here:
the **documentation check** reads each of the five fixed-type entries' own
`- verified-at:` line and asserts the four required elements are present (old→new where
a replacement happened, the reason trail back to round 16, the access date, the receipt
path), then confirms the receipt file exists on disk.

## 1. `mongol.md` — round-8 hard-fail `rubruck.html` does not reproduce (patch row 4 / map idx 67)

| # | fixer claim (receipt `civ/mongol.md`) | my independent re-run | verdict |
|---|---|---|---|
| 1 | round-8 sweep: `depts.washington.edu/silkroad/texts/rubruck.html` classified `000` (connection class, retried once) | the classification is quoted from `reports/round-8/metadata/m04-civ-58-76.md` §4 run A; not re-run by this seat (historical file, read-only) | read-only |
| 2 | re-attempt: 4/4 HTTP 200, **289,660 B**, sha256 `2bcad68dcd9a5a379b61afb30abc95d57182f680816902d24d79cda89067efc6` | **200, 289,660 B** body, sha256 **`2bcad68d…9067efc6`** — identical; `<title>William of Rubruck's Account of the Mongols</title>` | exact |
| 3 | old → new: **unchanged** (no replacement needed; a mirror would be churn) | the entry cites the same URL; my sweep of the entry shows **10/10 URLs at HTTP 200**, zero non-2xx | exact |
| 4 | fallback mirror named but not written into the entry | `web.archive.org/web/20261012155833/…/rubruck.html` — named in the receipt only; entry bytes carry the original locator | consistent |
| 5 | after-hash `e60b3903…c14c1163` (1-line edit: verified-at) | delivered sha256 → **identical**; patch `sha256_before` `0c85e10f…` == `git show f30b6f8:…/mongol.md` sha256 | exact |
| 6 | entry records the re-attempt, 4/4 samples, content-verification of the cited passages, receipt pointer | line 18 `- verified-at:` carries: round-8 origin, the 000 class, "4/4 samples HTTP 200", the content check named by topic, "kept unchanged (no replacement needed)", `reports/round-17/civ/mongol.md` | exact |

**Verdict: VERIFIED — byte-exact on the delivered body, digest, entry hash and doc
elements.** This is the strongest form of "debt retired": the cited locator is live and
content-verified, and nothing was replaced.

## 2. `muisca.md` — 4 hard-fail `muysca.cubun.org` locators live (patch row 5 / map idx 68)

| # | fixer claim (receipt `civ/muisca.md`) | my independent re-run | verdict |
|---|---|---|---|
| 1 | all four URLs HTTP 200 across three samples, sizes `nyia` 30,692 / `chunso` 25,827 / `chyquy` 33,028 / `psihipqua` 32,263 B and digests `68342c14…`, `12a05c94…`, `1220ae0c…`, `a2568b59…` | my four fetches → **200 ×4**, on-disk bodies **30,692 / 25,827 / 33,028 / 32,263 B**, sha256 **`68342c14f9cc6479…` / `12a05c944c6745a9…` / `1220ae0c56216328…` / `a2568b599786ed9c…`** — all four digests identical | exact |
| 2 | scheme finding (negative): `https://muysca.cubun.org/{nyia,chunso}` times out `000` | `https` probes → **000** on both (20 s timeout each) | reproduces |
| 3 | locator strings unchanged (http-only host; do not "upgrade") | entry line 6 says exactly that; the four `http://` URLs are in the source table | exact |
| 4 | remaining cited links keep their classes: arXiv 200, Cambridge repository 200, HathiTrust 403, Antiquity DOI 429 | my sweep: `arxiv.org/html/0812.0574v3` **200**, `repository.cam.ac.uk/…/download` **200**, `catalog.hathitrust.org/Record/101231772` **403**, `doi.org/10.1017/S0003598X00047918` **429** | exact ×4 |
| 5 | after-hash `417b7086…b4237064` (2-line edit) | delivered sha256 → **identical**; before-hash `b1f013ac…` == `git show f30b6f8:…/muisca.md` sha256 | exact |
| 6 | entry records the re-attempt + trail (`m04:87-90`, round-16 map entry 68, `060-071.md:95`) + the scheme caveat | line 6 carries all three references, the "three independent samples" wording, the folio-anchor re-check, and the do-not-upgrade sentence | exact |

**Verdict: VERIFIED — four URLs, four matching digests, the negative scheme claim
reproduces, the adjacent-link classes reproduce.**

## 3. The 5 attempt rows' documentation check (assignment item)

Rows: `inuit`, `maya-classic`, `mesoamerica-primary-sources` (group A — verified in
`verify-1.md`) and `mongol`, `muisca` (group B — above). Required elements per row:
(a) the entry's own `- verified-at:` line documents the attempt (fix or retirement) in
place; (b) where a locator was replaced, old → new appears in the entry bytes;
(c) the reason trail back to the round-16 debt is cited; (d) the round-17 receipt path
exists and the row's `evidence_path` points at it.

| row | (a) entry documents | (b) old→new in entry | (c) round-16 trail | (d) `evidence_path` exists |
|---|---|---|---|---|
| inuit | yes — line 5 | yes — old URL → pageplace preview URL | `m03:67,109`, `v03:72`, map entry 44 | `reports/round-17/civ/inuit.md` ✓ |
| maya-classic | yes — line 17 | n/a (couples repair: pointer added, lexicon untouched) | `review-C08.md:182` → `060-071.md:88,119` → receipt | `reports/round-17/civ/maya-classic.md` ✓ |
| mesoamerica-primary-sources | yes — line 38 (+ [HIG] line 30 caveat) | yes — dead Lilly URL kept as trail, replaced by ScholarWorks + Wayback raw | `060-071.md` (row 62) | `reports/round-17/civ/mesoamerica.md` ✓ |
| mongol | yes — line 18 | n/a (kept unchanged, said so) | `060-071.md:94,125`, `m04` §4 | `reports/round-17/civ/mongol.md` ✓ |
| muisca | yes — line 6 | n/a (locators kept, said so) | `m04:87-90`, map entry 68, `060-071.md:95` | `reports/round-17/civ/muisca.md` ✓ |

All five receipts exist on disk (`os.path.exists` over the patch's `to.evidence_path`
→ 12/12 present, all rows). **Verdict: the 5 attempt rows' documentation holds** — each
attempt is written into the artifact it changes, with date, command class, outcome and
receipt pointer.

## 4. Counting-command reproduction (assignment item)

- `ls corpus/knowledge/civilizations/*.md | wc -l` → **94** — run 2026-10-18 at
  ≈10:19Z and again at 10:32:53Z (the two stamps this seat kept; the value is stable
  because round-17 fixes edited entry bytes, not the entry set). This is the round-16
  map's own `counting_command`; the map's `count` field is 94 with 94 entries
  (82 `current` + 12 `stale-documented` pre-patch), which my recount confirms.
- **Second 94, reconciled:** the never-swept seven's baseline URL census. Sum of
  `distinct_before` over the 7 never-swept patch rows = **94**
  (persia 9 + polynesia 26 + rapa-nui 9 + rome 12 + ryukyu 12 + scythian 12 + siam 14),
  computed from the patch by this seat. My extraction from the *post-fix* entry bytes
  yields **95** distinct URLs for those seven — exactly the 94 baseline plus the one
  URL round 17 added (the persia-sasanian Wayback fallback; academia.edu −1 and
  edspace +1 cancel, as the persia receipt's §6 states: "distinct-URL count after
  edit: 10 (was 9)"). So both 94s in play — entries and baseline URLs — reproduce and
  their difference is accounted for, not a discrepancy.

## 5. Board checks this seat re-ran

- Patch `from_` vs `reports/round-16/civ-map.json` rows: **12/12 byte-equal** (fields
  `status`, `verified_at`, `command`, `reason`); `idx_round16_1based` matches the filed
  order for all 12.
- **Round-16 map untouched:** sha256 `07cabb69b4a41c51b74767212a07ba4ffae3c09ef8c2571abd954b37342cb943`
  (equal to the patch's declared target sha); `git status --porcelain reports/round-16/
  reports/round-17/` → 0 lines.
- `sha256_before` (12/12) == `git show f30b6f8:…` blobs; `sha256_after` (12/12) ==
  delivered bytes. No filed receipt of rounds 8–17 was written by any check in this
  seat.
- Round-18 map revision (landed 10:27:26Z, i.e. after this seat's checks began):
  `reports/round-18/civ-map-r18.json` — its `applied_patch.sha256` equals the patch
  file's sha256 (`79ceafab…76e77e`), its 12 transitions match the patch `to` blocks on
  status/command/date (12/12), its 82 carried rows are field-identical to the round-16
  map rows (0 mismatches), and all 20 `evidence_pins` resolve and hash correctly.
  Cross-check run by this seat; full detail in `verify-4.md` §4.
- Live-wave cross-reference: a sibling C seat's scratch
  (`.scratch/r18c09/probe-run1.log`, 10:23Z) independently reports the same values this
  seat measured for six of the twelve rows — cited for cross-reference only, not used
  as evidence.

## 6. Findings carried to the parent

- **F-C04-1 (documentation, minor):** in `muisca.md` the entry's own sentence says the
  four locators were live "across three independent samples" — that three-sample claim
  is the fixer's protocol; this seat re-ran **one** independent sample per URL (plus a
  second negative sample for the https variant). The claim reproduces at 1/1 samples
  per URL with identical digests, so the entry statement is corroborated, not
  independently counted.
- **F-C04-2 (route to the map):** the two retained-trail URLs (`inuit` old Dorais 404,
  `mesoamerica` old Lilly 404-by-design) will report non-200 on every future sweep.
  The map revision should carry their disposition in the reason/command column rather
  than letting a later counting pass read them as rot. (Same class as F-C03-1's openn
  note in `verify-1.md`.)

## 7. Compliance

Writes: **this file only**, plus gitignored scratch under `.scratch/r18c03/` (all scratch
bytes confined to `.scratch/`; `export TMPDIR=$PWD/.scratch` for the scripted passes, the
ad-hoc fetches wrote to `.scratch/r18c03/bodies/` directly). No corpus entry, map,
receipt, tool or earlier-round byte edited; no git mutation; no commit; no writes
outside the lane repo. Sibling scratch read for cross-reference only.
