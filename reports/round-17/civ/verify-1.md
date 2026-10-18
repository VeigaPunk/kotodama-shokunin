# R17-V01 — independent verification of round-17 C-fixer evidence (group 1 of 2)

- Verifier seat: **C R17-V01** (round-17 C-verifiers). This file covers the fixer
  evidence for **`inuit`, `maya-classic`, `mesoamerica-primary-sources`, `mongol`,
  `muisca`, `persia-sasanian`** (six of the twelve round-16 stale entries). Sibling
  verdict `verify-2.md` (R17-V02) covers `rapa-nui`, `rome`, `siam-thai`,
  `polynesia-navigation`, `ryukyu`, `scythian-saka`.
- Date: 2026-10-18; verification window ~09:19–09:32Z (all stamps UTC). Worktree
  HEAD during verification `9b49a4a`; a live 64-worker wave, so every corpus hash
  below is re-checked at write time and pinned in the verdict text.
- Method, stated before results. For every fixer receipt I (1) read the claims and
  the commands it quotes; (2) re-ran the fetches myself (M04 method where the fixer
  used it; the fixer's own stricter forms — `-k`, `--compressed`, range requests —
  where its claim depends on them); (3) re-downloaded and re-hashed every artifact
  whose digest was claimed; (4) spot-checked the entry text in
  `corpus/knowledge/civilizations/<entry>.md` against the claimed old→new locator,
  reason trail, and access date; (5) re-ran the claimed negative sweeps and gates.
  My own M04-method sweep of all 188 cited URLs across the twelve entries (16
  workers, retry once on 000) is archived at `.scratch/v01/sweep12.json`
  (2026-10-18T09:19Z); pre-fix copies + sha256 of all twelve entries at
  `.scratch/verify-baseline/` (09:15:49Z), so every diff below is against bytes I
  captured before the first fixer edit landed.
- **NON-CANON.** Verification only: no canon, rank, rights/clearance, freshness or
  promotion ruling is made or implied. "Verified" below means *the fixer's dated,
  command-carried claims reproduce on my independent re-run*, not that the sources'
  scholarship is current or correct.

## Summary table (group 1)

| entry | fixer receipt | disposition | my verdict | corpus sha256 at verification |
|---|---|---|---|---|
| inuit | `reports/round-17/civ/inuit.md` | stale-fixed (locator replaced) | **VERIFIED** — byte-exact | `52c5a11b…ef0c5d` |
| maya-classic | `reports/round-17/civ/maya-classic.md` | stale-fixed (couples gap closed) | **VERIFIED** — byte-exact | `d9608d84…8ce67b5` |
| mesoamerica-primary-sources | `reports/round-17/civ/mesoamerica.md` | stale-fixed (1 replaced, 2 retained w/ caveat, pin re-based) | **VERIFIED** — 12/12 checks exact | `d04d8913…1d0db530` |
| mongol | `reports/round-17/civ/mongol.md` | stale-fixed (locator live, unchanged) | **VERIFIED** — byte-exact | `e60b3903…c14c1163` |
| muisca | `reports/round-17/civ/muisca.md` | stale-fixed (4 locators live, unchanged) | **VERIFIED** — byte-exact | `417b7086…b4237064` |
| persia-sasanian | `reports/round-17/civ/persia-sasanian.md` | stale-fixed (2 locators fixed/fallback) | **VERIFIED** — tallies + artifacts exact | `20e7513e…40ca7e2e` |

Findings carried to the parent: **F-V01-1** (sed80 CDX overstatement — group 2),
**F-V01-2** (validator classification nuance, §7), **F-V01-3** (sed77 was internally
inconsistent in its first-read version; current version is consistent — §6).

---

## 1. inuit.md — Dorais 2010 dead locator repaired (receipt `civ/inuit.md`)

Fixer claims vs my independent re-run:

| # | fixer claim | my re-run (2026-10-18) | verdict |
|---|---|---|---|
| 1 | old locator 404 ×3, redirect to `jackmanlaw.utoronto.ca` | `curl -L` → **404**, effective `https://jackmanlaw.utoronto.ca/…pdf` | reproduces |
| 2 | new locator `api.pageplace.de/preview/…9780773581623….pdf` full fetch **200, 515,139 B, application/pdf** | **200, 515139, application/pdf** | exact |
| 3 | fetched copy sha256 `61388588ca884f514c3e29510fc4ba21cb3d14d0b849e2a728eb87502f5f660d`, 41 pages | my copy sha256 **`61388588…f5f660d`** (identical), `file` → 41 page(s) | exact |
| 4 | copyright page shows cited ISBN `978-0-7735-3646-3`; Contents present | my `pdftotext` → `isbn 978-0-7735-3646-3` (lines 260/283), Contents with all 10 chapters + appendices | exact |
| 5 | ToC chapters family / dialects / linguistic history / literacy | ch. 1 Eskaleut Family, ch. 3 Nunavik Dialect, ch. 4–5 Prehistory + Historical Sources, ch. 7 Literacy and Formal Education | exact |
| 6 | after-hash `52c5a11b7b7db949f8f93da199a34a0062a888a180e021b2a124558480ef0c5d` | **identical** | exact |
| 7 | provenance gate: 6 marks, findings=0, exit 0 | **identical** (`marks=6 mark-lines=6 findings=0 blocked=0`) | exact |
| 8 | in-file D-row URL range probe `206|1024|application/pdf` | **`206|1024|application/pdf`** | exact |
| 9 | rejected candidates: `mqup.ca/…9780773536463.php` 404; `muse.jhu.edu/book/22942` is a different book | mqup → **404**; muse.jhu → **200**, title `Project MUSE - Yellow Power, Yellow Soul` | reproduces |
| 10 | before-hash `312427a3…` = round-16 receipt bytes | my pre-fix baseline copy hashes `312427a3…0b` | exact |

Entry spot-check: the D row now carries the new locator (label "front matter and
contents preview"), the `- verified-at:` line carries the old→new URLs + round-8/9/16
reason trail (`m03:67,109`, `v03:72`, round-16 map entry 44), and the access line
records the 2026-10-18 probe. Head keys still parse 1:1 (5 keys). The entry's other
cited links keep their 2026-10-17 status, as the entry states.

**Verdict: VERIFIED (byte-exact on every claimed artifact).**

## 2. maya-classic.md — round-10 N2 couples gap closed (receipt `civ/maya-classic.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | pre-fix bytes `d3520973…`; gap reproduction `grep -inE 'sacbe|causeway|white road'` → 0 hits | baseline hash **`d3520973…`**; grep → exit 1, no output | exact |
| 2 | `[S]` Sacbe fetch: 200, 178,576 B, sha256 `94b6bdafaae439ccc171e6e1f3fe458bbebb8a0954a547609d2d4c0c5c567e90`; byte-identical to round-10's sha16 `94b6bdaf` | my fetch **200, 178576 B**, sha256 **`94b6bdaf…7e90`**; `reports/round-10/coverage/review-C08.md:176` records `Sacbe 94b6bdaf…` | exact |
| 3 | `[KH]` handbook: 200, 49,858,925 B, sha256 `2327b090ed3dfb0ef2b891786aef22a5612589253bdaf2a40b290604f9d238f2` | my own 49MB download: **identical size and sha256** | exact |
| 4 | KH thematic dictionary p. 99/151 (PDF p. 101): `bih ~ bij` "compare to sak-bih for lit. 'white-road' which is the Classic-period reflex of the causeways known as sakbeob in Yucatan"; `bihtuun` entry | my `pdftotext -f 101 -l 101` → both quotes present (page 101 exactly) | exact |
| 5 | after edit: 9 sacbe hit lines (was 0); §14 present at EOF; reciprocal couples pointer added | grep → **9 hits**; §14 at line 201; couples line names `transport-mobility-lexicon.md`; lexicon `:20` still names maya-classic (sacbeob) | exact |
| 6 | lexicon untouched, sha256 `86e5f9520e07e3ebb5d518183bb273d1ee8c22cca9c3ef1d35cf8fcef6d5aa70` | **identical**; not in `git status` | exact |
| 7 | after-hash `d9608d842ccb97da3514032d41a323016dc65c0039ff6396d4f96b7678ce67b5`, 208 lines, 10 distinct URLs, provenance 5 marks findings=0 | **all four identical** | exact |
| 8 | no frozen manifest pins this entry (`find tools/gates/frozen -name maya*` → 0) | **0** | exact |

**Verdict: VERIFIED (byte-exact).** The fix closes the round-10 N2 debt in the
pointer's direction (target built, pointer unchanged and now true) without touching
the lexicon or any filed artifact.

## 3. mesoamerica-primary-sources.md — 3 hard-fail URLs + pin drift (receipt `civ/mesoamerica.md`)

This is the receipt whose TLS diagnoses explain the strict-client 000s I also
observed. All 12 numbered claims re-ran exactly:

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | getty folio strict 000; `-k` **200, 267,502 B**; title `Book 12 Folio 19v| Digital Florentine Codex`; markers `19v`×19, `Book 12`×16, `Terraciano`×8 | **200, 267502**, title identical; markers **19 / 16 / 8** | exact |
| 2 | getty TLS: leaf `CN=florentinecodex.getty.edu`, issuer `InCommon Intermediate CA - OVG2C` not sent; `Verify return code: 21` | `openssl s_client` → issuer/CN identical, **rc 21** | exact |
| 3 | iif strict 000; `-k` **200, 3,499,309 B, application/pdf**, 16 pp., created 2013-04-02 | **200, 3499309**, pdfinfo 16 pp., `CreationDate … 2013-04-02` | exact |
| 4 | iif TLS: issuer `GlobalSign RSA OV SSL CA 2018` not sent; rc 21; SANs cover both hostnames | rc **21**, issuer identical; cert CN `www.iifilologicas.unam.mx` | exact |
| 5 | liblilly `-k` → **404, 146 B**, nginx `404 Not Found`; cert `CN=*.bio.indiana.edu` hostname mismatch | **404, 146**, title `404 Not Found`; openssl subject `CN=*.bio.indiana.edu` | exact |
| 6 | replacement article `scholarworks.iu.edu/…/3788` strict **200, 19,081 B**; author/firstpage 69/lastpage 88 | **200, 19081**; `John Frederick Schwaller`, `firstpage" content="69`, `lastpage" content="88` | exact |
| 7 | replacement PDF galley strict **200, 5,388,824 B** | **200, 5388824** | exact |
| 8 | Wayback raw snapshot `20210227003441id_` strict **200, 130,398 B**, sha256 `27d6a210bfc3a88da9015e52537c51f6b529411b361b3f333b3b5120cbae09ae` | **200, 130398**, sha256 **identical** | exact |
| 9 | controls: getty project page strict **200, 3,162,177 B**; iif `/estmesoam/` `-k` **200, 12,579 B** | **200, 3162177**; **200, 12579** | exact |
| 10 | dead-end control `indiana.edu/~liblilly/etexts/nahuatl/` **200, 318,019 B**, catch-all homepage | **200, 318019**, title `Indiana University Bloomington | Academics, research, and impact` | exact |
| 11 | pin drift: frozen round-3 inputs **both** `a916a4c2…` (32,633 B); `git show c610e0a` → `a916a4c2…`; `git show e1694ba` → `6d40a97d…` | all three hashes **identical** | exact |
| 12 | after-edit: hash `d04d8913…`, 49,538 B, distinct URLs 46→**49**, `to-verify` 12 unchanged; negative sweep rounds 9–16 hits only `060-071.md` (3) | **identical** (49 URLs, 12 marks, 49538 B); grep hits only `060-071.md` | exact |

Entry spot-check: revision 1.1→1.2 line, [FC]/[HIG] caveat appends, [MOL] old→new
replacement with the dead URL kept as plain-text trail, verified-at append, and the
known-open-items note all present; the reason trail names `060-071.md` and the
round-11 pin. The entry will keep failing a strict sweep on the two retained URLs by
design (server-side incomplete chains) — as the receipt says, a future map must read
the entry note, not the bare code.

**Verdict: VERIFIED (12/12 exact).**

## 4. mongol.md — rubruck.html re-attempt (receipt `civ/mongol.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | 4/4 samples 200, 289,660 B; body sha256 `2bcad68dcd9a5a379b61afb30abc95d57182f680816902d24d79cda89067efc6`; title `William of Rubruck's Account of the Mongols` | my fetch **200, 289660 B**, sha256 **identical**, title identical | exact |
| 2 | content markers: right-fastening quote ×1; `bocca` ×5; "All soothsayers are called cham" ×1 / `cham` ×7; tablet ×1; `Theodulus` ×4; "word of Mangu Chan to the lord of the French" ×1; `King Louis` ×4 | **1 / 5 / 1 / 7 / 1 / 4 / 1 / 4** — every count identical | exact |
| 3 | after-hash `e60b3903402034bcd897617fac589340fb9c70439a028583fbe193fec14c1163`; URL count unchanged (10) | **identical**; 10 distinct URLs | exact |
| 4 | negative sweep: `rubruck` in rounds 9–16 → only `060-071.md` + `civ-map.json` | **identical** (2 files) | exact |
| 5 | entry keeps round-16 reason trail + receipt pointer | verified-at line 18 names `reports/round-16/civ/060-071.md` and the receipt | exact |
| 6 | fallback mirror Wayback snapshot `20261012155833` 200 | (not re-fetched; fallback-only, not written into the entry — noted as unverified-by-me, non-material) | not re-run |

**Verdict: VERIFIED (byte-exact on all material claims; the fallback mirror claim
is informational and was not re-run).**

## 5. muisca.md — 4 muysca.cubun.org locators re-attempted (receipt `civ/muisca.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | 4 URLs 200; bodies nyia 30,692 B sha16 `68342c14f9cc6479`; chunso 25,827 B `12a05c944c6745a9`; chyquy 33,028 B `1220ae0c56216328`; psihipqua 32,263 B `a2568b599786ed9c` | my fetches: **30692 / 68342c14f9cc6479**; **25827 / 12a05c944c6745a9**; **33028 / 1220ae0c56216328**; **32263 / a2568b599786ed9c** — every byte count and sha16 identical | exact |
| 2 | anchor loop output (`Ms. 2923/158…` per page) | my re-run prints the **same output line-for-line** as quoted in the receipt | exact |
| 3 | https on all four → 000 (host http-only) | my parallel re-run: **000 ×4** | exact |
| 4 | rounds 9–15 sweep of `muysca.cubun\|rubruck\|florentinecodex.getty\|totonicapan_simonetta\|liblilly` → 0 matches | grep → **exit 1, 0 matches** | exact |
| 5 | adjacent probe: arXiv 200, Cambridge repo 200, HathiTrust 403, Antiquity DOI 429 | my sweep: muisca 6×200, 1×403, 1×429 — the two access-limited are exactly HathiTrust 403 / DOI 429 | reproduces |
| 6 | entry edits: 2 lines only (verified-at + [DG] row), reason trail kept | diff vs my baseline: exactly those 2 lines; trail names `m04:87-90`, round-16 map entry 68, `060-071.md:95` | exact |
| 7 | post-edit hash left as `TREE_AFTER` placeholder (unmaterialized by design) | actual current hash: **`417b7086b5b3e8270b8509e17223c4bc966bd60d7d82cc444bf5a979b4237064`** (recorded here; not a claim failure) | recorded |
| 8 | observation OBS-1: entry writes `Ms. II/2923` vs live `Ms. 2923.`; `II/2923` occurs only in this entry in-repo | my grep: `II/2923` in `corpus/` → only `muisca.md:88`; elsewhere only in the round-17 receipt itself | reproduces |

**Verdict: VERIFIED (byte-exact).** Note the post-edit hash is recorded here
because the fixer deliberately left it to the integrating parent; the tree value at
my verification is the `417b7086…` above.

## 6. persia-sasanian.md — never-swept 9-URL set, 2 locators fixed (receipt `civ/persia-sasanian.md`)

| # | fixer claim | my re-run | verdict |
|---|---|---|---|
| 1 | 9 distinct URLs; tally 6×200, 1×429, 1×403, 1×000 | my M04-method sweep: **6×200, 1×429, 1×403, 1×000** — identical classification, same URLs (429 = Cambridge DOI; 403 = academia.edu; 000 = avesta.org) | exact |
| 2 | avesta.org 000 = TLS certificate **expired** (`notAfter Oct 9 23:59:59 2026 GMT`) | `openssl s_client` → **`Verify return code: 10 (certificate has expired)`** | exact |
| 3 | replacement `Compareti_SR14_2016_71_83.pdf`: 200, 948,943 B, title `OBSERVATIONS ON THE ROCK RELIEFS AT TAQ-I BUSTAN…` | **200, 948943 B**; first page carries exactly that title | exact |
| 4 | Crossref: `10.1017/S0041977X00133063` = Boyce, "Some Reflections on Zurvanism", BSOAS 19(2) 304–316, 1957 | (not re-fetched by me; DOI-handle resolution checked for the other DOI pattern in group 2 — noted as not re-run) | not re-run |
| 5 | after-hash `20e7513e1f3b288e167f2cd56163caba2cbc238c92b0b6524b655a6f40ca7e2e`; 4-line diff; distinct URLs 9→10; provenance 1 mark findings=0 | **all identical** (hash, `4 4` numstat, 10 URLs, `marks=1 findings=0 exit 0`) | exact |
| 6 | entry edits: line 14 (avesta unreachable note + archived fallback), line 19 (academia→edspace), line 22 (verified-at + round-16 reason token), line 202 (consistency: "reachable … only through its archived copy") | diff vs baseline confirms exactly these 4 lines; reason trail names `072-083.md §3` | exact |

**Verdict: VERIFIED.** (The two Crossref metadata rows in the receipt were not
re-fetched by me; the corresponding content-check pattern was independently
reproduced in group 2 for rome's two DOIs, and the sweep/artifact claims here are
exact.)

---

## 7. Cross-cutting findings and notes (group 1)

- **F-V01-2 (validator classification nuance, informational).** In
  `reports/round-17/validation.json` the runner classifies `inuit` (and `persia`,
  `muisca`, `mongol`, `rome`) as `attempted`, with `fixed_count = 3`
  (`maya-classic`, `mesoamerica-primary-sources`, `siam-thai`). The observable
  cause: those entries keep their **old URL inside the old→new trail text**, so a
  classifier requiring "old absent from current bytes + new present" reads them as
  attempted rather than fixed. Claim C passes either way (`passed: true`,
  `failures: []`), and the underlying facts (replacement present, content-verified,
  trail documented) are verified above; flagged so the final map/LOG wording does
  not undercount the locator swaps.
- **Byte-count reporting nuance (sed77, informational).** rome's sweep reports
  `size_download` under `--compressed` (wire size), so its byte column (e.g. OCRE
  11,046 B) differs from an uncompressed re-run (80,524 B) **while the body sha256
  matches exactly**. Re-runners should compare the digest column, not raw byte
  counts, when reproducing that receipt. (Detail in group 2.)
- **Versioning note (sed77).** The first version of `civ/sed77.md` I read (207
  lines, 09:2xZ) was internally inconsistent about whether rome's entry was edited
  (§4.4/§7.1/§7.3 said "not performed" while §1 said edited); the current version
  (237 lines, 09:28Z) is consistent and matches the tree (`0b29e05c…`, one-line
  edit). Resolved by the fixer seat before my verdict; no finding stands.
- **Shared-worktree honesty.** Every receipt read here correctly declares sibling
  seats' in-flight edits as not its own, and every `git status`-based scope claim I
  re-ran matched at its stated time.

## 8. Limits of this verification

- Point-in-time: all re-runs are 2026-10-18 ~09:19–09:32Z on one network path.
  Link status and dynamic-page bytes are not invariants; static resources reproduced
  byte-exactly, dynamic pages can vary (see group 2, rapa-nui).
- I re-ran the material claims of each receipt; a small number of secondary rows
  (mongol's Wayback fallback; persia's Crossref metadata lines) were not re-fetched
  and are marked "not re-run" above.
- My sweep uses the M04 regex, which truncates URLs at `)`; rome's OCRE URL is the
  one entry affected (group 2). Fixer receipts that use balanced-paren extraction
  are not affected.
- "Verified" here means reproduction of dated, command-carried claims — it is not a
  freshness, rank, canon, or rights verdict; the freshness pause stays in force.

— C R17-V01, round-17 C-verifier, 2026-10-18. Scratch evidence:
`.scratch/v01/` (`sweep12.json`, `sweep12.py`, per-claim fetch bodies and logs).
