# R18-C06 — independent verification of the round-17 civ patch, group 4 of 4 (never-swept B + 12-row roll-up)

- Verifier seat: **C R18-C06**. Covers the **never-swept group B** rows of
  `reports/round-17/civ/map-patch.json`: **`ryukyu`, `scythian-saka`, `siam-thai`**
  (map indices 81–83), and closes the four-seat series with the **12-row roll-up**,
  the **94 reconciliation** and the **board-integrity checks**. Sibling seats:
  `verify-1.md` (C03: inuit, maya-classic, mesoamerica), `verify-2.md` (C04: mongol,
  muisca + attempt documentation), `verify-3.md` (C05: persia-sasanian,
  polynesia-navigation, rapa-nui, rome).
- Date: 2026-10-18; window **10:19–10:33Z** (UTC). Lane HEAD `c66ac3c`; fixes at
  `3dd3754`; pre-fix bytes `f30b6f8`.
- Assignment (verbatim): *"C R18-C03..C06 (verify x4): independently re-run each
  transitioned row's new evidence (fetch the replacement URLs, spot-check); verify the
  5 attempt rows' documentation; counting command reproduces 94;
  reports/round-18/civ/verify-{1..4}.md."*
- **NON-CANON.** Access-status verification only.

## 0. Method

As in `verify-1.md` §0 / `verify-3.md` §0: independent re-fetch of every replaced or
re-pinned locator (old and new), independent full-entry sweep (193 URLs over the 12
rows; per group here the three entries' 38 URLs), on-disk byte counts + sha256,
negative controls for "moved host" claims, and diffusion against filed git bytes.

## 1. `ryukyu.md` — never-swept sweep, no replacement needed (map idx 81)

Patch row claims: `distinct_before` 12 (11 live, 1 bot-block 403 MDPI, 0 hard fail);
receipt `civ/sed78.md`.

| # | fixer claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | 12/12 URLs status-checked; 11 × 200 | my sweep: **12/12 returned 200** | my sample is one better than claimed (see F-C06-1) |
| 2 | 1 × 403 bot wall at `www.mdpi.com/2077-1444/10/5/298` (content re-verified via a second agent; archive fallback named) | my fetch → **200, 2,224 B body** which is *not the article*: a JS/bot challenge page (`<meta http-equiv="refresh" content="5; URL='/2077-1444/10/5/298?bm-verify=AAQ…'"`). The substance of the receipt's classification — **bot wall, not rot** — reproduces; only the status code differs by vantage/time. Sibling R18-C09's independent probe (10:23Z) recorded **403 / 398 B** for the same URL | reproduces in substance — **F-C06-1** |
| 3 | no locator replaced; no 404/000 | my sweep has 0 × 404, 0 × 000; the entry's `http://doi.org/10.18874/jjrs…` and all institutional pages resolve | exact |
| 4 | after-hash `424fcbb5…819afa5`; before-hash `de541d33…d88883` | delivered → **identical**; `git show f30b6f8:…/ryukyu.md` → **`de541d332cced7ae…`** | exact |
| 5 | entry: status/locator receipt only, not a freshness verdict | line 6 states exactly that plus the freshness pause reference | exact |

**Verdict: VERIFIED** (with F-C06-1 naming the code-class nuance).

**Finding F-C06-1 (bot-wall code variance, informational):** MDPI serves the ryukyu
article URL as a **JS challenge page** whose status alternates (my sample 200 with a
2,224-byte challenge body; the round-17 receipt and a sibling round-18 seat saw 403).
Either reading is "not rot, not article content at curl level"; a future counting pass
should classify this row by *challenge-page detection* (tiny body + `bm-verify` /
refresh meta), not by the code alone.

## 2. `scythian-saka.md` — sweep + 1 permanent-301 re-pin (map idx 82)

| # | fixer claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | 12/12 swept: 11 × 200, 1 × 403 Cloudflare at academia.edu, 0 hard fails | my sweep: **11 × 200, 1 × 403** (`academia.edu/104775728/`) — exact tally | exact |
| 2 | Leiden locator re-pinned to its permanent 301 target: `access/item%3A2882853/view` → `handle/1887/16379`; new = 200, **8,911 B** | old URL follows to **`…/handle/1887/16379?rep=01&m=9940747172202711`**; new `…/handle/1887/16379` → **200, 8,911 B** — identical body (`92adb908b86df1a1…`) for old and new | exact |
| 3 | content markers verified across the Herodotus 4A/4B/4C/7B pages, Lubotsky record, Rudenko/Rolle catalogues, AJA review, Iranica "Khotan iv", two Wikipedia trails | my sweep: all eleven → 200 with the pages' own titles/bodies (e.g. Iranica 108,607 B, AJA 34,692 B, Herodotus 4A–4C 42,727/70,253/76,005 B) | consistent |
| 4 | after-hash `cb3a6428…b3ab5c51`; before-hash `aff3ca0a…72e95e00` | delivered → **identical**; `git show f30b6f8:…/scythian-saka.md` → **`aff3ca0aa3a31e47…`** | exact |

**Verdict: VERIFIED — tally, the 301 target's body size and the entry hash are exact.**

## 3. `siam-thai.md` — sweep + 2 canonical-301 re-pins (map idx 83)

| # | fixer claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | 14/14 swept: 12 live (incl. 2 via permanent 301s re-pinned), 2 Cloudflare 403s | my sweep: **14 URLs → 11 × 200, 1 × 202** (`doi.org/10.1515/9783110401981-013`, DOI accepted) **, 2 × 403** (`cambridge.org/9781316641132`, `blogs.loc.gov/law/2025/07/…`) = 12 live / 2 blocked / 0 hard fail | exact |
| 2 | `culturalatlas.sbs.com.au/thai-culture/thai-culture-naming` → `theculturalatlas.org/…`; new = 200, **118,615 B** | old URL follows to the new host; new URL → **200, 118,615 B** body — byte-exact to the claim (both old and new end at the same body, `4f673f505d0276a1…`) | exact |
| 3 | `publishing.cdlib.org/ucpressebooks/view?docId=ft3j49n8h7&brand=ucpress` → `…/public/book/many-ramayanas-…-south-asia.html`; new = 200, **1,657,019 B** | old URL follows to the `.html` target; new URL → **200, 1,657,019 B** body — byte-exact | exact |
| 4 | Cloudflare 403 walls kept with retries recorded; receipt corrected mid-run hash | the two 403s reproduce (1,302-byte-class challenge bodies on both hosts); no hard-fail row in my sweep | exact |
| 5 | after-hash `8bef2a5b…7cb6c733`; before-hash `cf9269bc…14ca06` | delivered → **identical**; `git show f30b6f8:…/siam-thai.md` → **`cf9269bcaa2ddef9…`** | exact |

**Verdict: VERIFIED — both canonical 301 re-pins reproduce byte-exact on the target
side, and the tally reproduces exactly.**

## 4. Twelve-row roll-up (this seat's close of the series)

All numbers below were computed by this seat from the patch file, the filed map, git
blobs and the delivered working tree in this window.

| row (map idx) | group | patch status | evidence re-run seat | verdict |
|---|---|---|---|---|
| inuit (44) | fixed-type | stale-fixed | C03 | verified (byte-exact) |
| maya-classic (61) | fixed-type | stale-fixed | C03 | verified (byte-exact, 2 source digests) |
| mesoamerica-primary-sources (62) | fixed-type | stale-fixed | C03 | verified (12 checks) + F-C03-1 openn |
| mongol (67) | fixed-type | stale-fixed | C04 | verified (byte-exact) |
| muisca (68) | fixed-type | stale-fixed | C04 | verified (4/4 digests) |
| persia-sasanian (77) | never-swept | stale-fixed | C05 | verified + F-C05-1 (Wayback byte variance) |
| polynesia-navigation (78) | never-swept | stale-fixed | C05 | verified (26/26 tally exact) |
| rapa-nui (79) | never-swept | stale-fixed | C05 | verified (9/9 tally exact) |
| rome (80) | never-swept | stale-fixed | C05 | verified (12/12 after paren correction) |
| ryukyu (81) | never-swept | stale-fixed | C06 | verified + F-C06-1 (MDPI challenge code) |
| scythian-saka (82) | never-swept | stale-fixed | C06 | verified (tally + re-pin exact) |
| siam-thai (83) | never-swept | stale-fixed | C06 | verified (2 re-pins byte-exact) |

**Patch-integrity results (all seats, re-stated for the map builder):**
`from_` rows byte-equal the filed round-16 map **12/12**; `sha256_before` ==
`git show f30b6f8:…` **12/12**; `sha256_after` == delivered bytes **12/12**;
`map-patch.json` `summary.status_counts` (`stale-fixed` 11, `current` 1) matches the
per-row `to.status` values; `stale_documented_remaining: 0` matches a post-patch map
state in which the only 12 `stale-documented` rows (82 `current` + 12 = 94) are all
dispositioned.

**Counting-command reproduction (assignment item, joint with C04):**
`ls corpus/knowledge/civilizations/*.md | wc -l` → **94** (this seat's run at
2026-10-18 10:32:53Z; C04 records two earlier runs); the never-swept baseline URL
census sums to **94** from the patch (`distinct_before` 9+26+9+12+12+12+14), and my
post-fix extraction of those seven entries gives **95** = 94 + the one URL round 17
added (persia Wayback fallback). Both 94s therefore reproduce; no unexplained delta.

**Board integrity:** `reports/round-16/civ-map.json` sha256
`07cabb69b4a41c51b74767212a07ba4ffae3c09ef8c2571abd954b37342cb943` — byte-equal to the
sha the patch declares as its target (so the filed map was not in-place edited);
`git status --porcelain reports/round-16/ reports/round-17/` → **0 lines** (no filed
round-16 or round-17 byte changed since the fixes landed).

### Round-18 map revision cross-check (`reports/round-18/civ-map-r18.json`)

The revision landed at **10:27:26Z** (`built_by` "CIV R18-C01/C02 map revision";
94 entries; `status_counts` `{current: 83, stale-fixed: 11}`; `stale-documented: 0`;
`transitions_applied` 12, `rows_carried_verbatim` 82; every transition also carries
`terminal_status: current`). Re-checked by this seat at 10:36Z against the patch and the
filed round-16 map (all read-only, in-repo):

| check | method (2026-10-18) | result |
|---|---|---|
| the revision declares the patch it applied | `sha256sum reports/round-17/civ/map-patch.json` vs `applied_patch.sha256` | **match** — `79ceafabac9fd84d6bec5cb701e3d1791b075e5e1300d7164126e40f9876e77e` |
| 12 transitions == patch `to` blocks (`status`, `command`, `verified_at`) | python field compare over `transitions` + `entries` | **12/12 match**, 0 mismatches |
| 82 unpatched rows carried verbatim | field compare over `status`, `verified_at`, `command`, `reason`, `evidence_path` | **82/82 identical**, 0 field mismatches |
| date + command on every transitioned row | `entries[].verified_at` / `.command` | **12/12** present (`verified_at` = 2026-10-18) |
| evidence pins | `sha256sum` over the revision's 20 `evidence_pins` paths | **20/20 resolve and hash correctly** |
| fix-receipt pins | `sha256sum` over the 12 `transitions[].fix_receipt` paths vs `fix_receipt_sha256` | **12/12 correct** |
| post-fix entry hashes | `sha256sum corpus/knowledge/civilizations/<entry>` vs `transitions[].entry_sha256_after` | **12/12 match** (and equal to the patch's `sha256_after` values) |
| counting command | `ls corpus/knowledge/civilizations/*.md \| wc -l` | **94** = the revision's `count` field |

So the delivered revision is a faithful, append-only application of the verified patch:
the transitions it carries are exactly the transitions this four-seat series re-ran, and
the rows it does not touch are field-identical to the filed round-16 map.

**Scope note (important for the parent):** the revision was built at 10:27:26Z, i.e.
*before* this seat's findings were filed; it does **not** carry F-C03-1
(`openn.library.upenn.edu` unreachable), F-C05-1 (Wayback replay byte variance) or
F-C06-1 (MDPI challenge-page code). Those are new observations from the verification
pass, to be routed by the parent into a later revision or a round-19 work item — the
revision under test is not deficient for their absence.

## 5. Findings carried to the parent

- **F-C06-1** — MDPI bot wall reports as 200-with-challenge-page in this seat's sample
  and 403 in the receipt/sibling sample; substance agrees, code does not. Classify by
  challenge detection (tiny body + `bm-verify`), not code alone.
- **F-C06-2 (route to the map)** — the sweeps in this round and round 17 are
  point-in-time, single-vantage, one-sample (mine) vs multi-sample (fixers'). Where the
  two disagree the disagreement is always *better* availability on the later sample
  (MDPI 403→200-challenge) or code-class noise (429/403 walls). No claim in the patch
  was falsified; the map should carry the sweep date and method per row, as the patch
  rows already do.
- **F-C06-3 (informational)** — `summary.never_swept_7.independent_sweep_agreement`
  ("81/81 comparable rows … 0 unexplained divergences") is a *fixer-era* statement; the
  round-18 verify seats re-ran all 95 post-fix URLs and reproduce the classes, with the
  three nuances named above (F-C05-1, F-C06-1, and rome's paren artifact). No
  reconciliation failure.

## 6. Compliance

Writes: **this file only**, plus gitignored scratch under `.scratch/r18c03/` (all
scratch bytes confined to `.scratch/`; `export TMPDIR=$PWD/.scratch` for the scripted
passes, ad-hoc fetches written directly into `.scratch/r18c03/bodies/`). No corpus
entry, map, receipt, tool or earlier-round byte edited; no git mutation; no commit; no
writes outside the lane repo; sibling scratch cited as cross-reference only.
