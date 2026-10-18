# R18-C05 — independent verification of the round-17 civ patch, group 3 of 4 (never-swept A)

- Verifier seat: **C R18-C05**. Covers the **never-swept group A** rows of
  `reports/round-17/civ/map-patch.json`: **`persia-sasanian`,
  `polynesia-navigation`, `rapa-nui`, `rome`** (the first four of the seven
  never-swept entries, map indices 77–80). Sibling seats: `verify-1.md` (C03),
  `verify-2.md` (C04), `verify-4.md` (C06: `ryukyu`, `scythian-saka`, `siam-thai` +
  12-row roll-up).
- Date: 2026-10-18; measurement window **10:19–10:33Z** (UTC). Lane HEAD `c66ac3c`;
  fixes applied at `3dd3754`; pre-fix bytes = `f30b6f8` (round-16 close).
- Assignment (verbatim): *"C R18-C03..C06 (verify x4): independently re-run each
  transitioned row's new evidence (fetch the replacement URLs, spot-check); … counting
  command reproduces 94; …"*
- **NON-CANON.** "Verified" = the fixer's dated, command-carried claims reproduce on
  this seat's independent re-run. Status is an access outcome, not a freshness or
  scholarship verdict (both the patch and the entries say so themselves).

## 0. Method

Protocol as in `verify-1.md` §0. For this group the core is an **independent full
sweep of every cited URL in the entry** (not just the replaced ones): one sample each,
8-way parallel, `-L --compressed --max-time 25`, UA `kotodama-r18-c-verify/1.0`,
scratch `.scratch/r18c03/sweep.json`; plus **targeted multi-sample re-probes** of every
replacement/fallback locator, with on-disk byte counts and sha256, and a **negative
control probe** wherever the claim is "host-wide bot wall" or "record exists". Where my
first pass disagrees, the disagreement is re-run against the exact entry URL before
being reported (this happened for rome's balanced-paren OCRE id — §4).

## 1. `persia-sasanian.md` — never-swept sweep + 1 replacement + 1 archive fallback (map idx 77)

Patch row: `stale-documented → stale-fixed`; sweep tally claimed `distinct_before` 9
(6 live, 2 bot-block, 1 hard-fail); receipt `reports/round-17/civ/persia-sasanian.md`.

| # | fixer claim | my independent re-run (2026-10-18) | verdict |
|---|---|---|---|
| 1 | `www.avesta.org/mp/grb.htm` primary: **000**, TLS certificate expired (`notAfter=Oct 9 23:59:59 2026 GMT`), 9/9 failed samples | primary → **000, 0 B**; `openssl s_client` → `notAfter=Oct  9 23:59:59 2026 GMT`, `subject=CN=avesta.org` — the same certificate fact | exact |
| 2 | archived fallback `web.archive.org/web/20260915232122/https://www.avesta.org/mp/grb.htm`: 200, **127,643 B**, `<title>Greater Bundahishn [introduction]`, links the cited chapters | 200, title and chapter links **reproduce exactly** (`grb1.htm#chap1` ×4, `grb12.htm#chap18`, `grb27.htm#chap28`, `grb27.htm#chap36`); **body bytes differ: 127,638 / 127,638 (two `--compressed` samples) and 127,640 (no compression)** | reproduces in substance; byte count see **F-C05-1** |
| 3 | `academia.edu/125247107/` old locator 403 → replaced | old URL → **403, 5,469 B**; the entry no longer carries it as the locator | reproduces |
| 4 | replacement `edspace.american.edu/…/Compareti_SR14_2016_71_83.pdf` 200, application/pdf, **948,943 B** | **200, 948,943 B** on disk, `file` → PDF | exact |
| 5 | 4 PDFs retrieved, title/page-count content-checked; Cambridge DOI 429 bot-block | my sweep: 8 × 200 + 1 × 429 (`doi.org/10.1017/S0041977X00133063`) + 1 × 000 (avesta primary); the Sasanika PDFs (2928181 / 536387 / 976223 B) and the SR13 companion (682753 B) all 200 | consistent |
| 6 | post-edit distinct-URL count **10** (was 9: −1 academia, +1 edspace, +1 snapshot) | my extraction from the delivered entry → **10** distinct URLs | exact |
| 7 | after-hash `20e7513e…40ca7e2e`; before-hash `9d0a65e3…` | delivered sha256 → **identical**; `git show f30b6f8:…/persia-sasanian.md` → **`9d0a65e3…`** | exact |

**Verdict: VERIFIED** (with F-C05-1 on the snapshot byte figure).

**Finding F-C05-1 (byte-count variance, informational but worth a map note):** the
Wayback replay of a *fixed snapshot* is not byte-stable across fetches. My three
fetches of `…/20260915232122/https://www.avesta.org/mp/grb.htm` returned 127,638,
127,638 and 127,640 bytes, while the receipt records 127,643. The mechanism is
identified: the replayed body carries the Wayback banner line

```
     INTERNET ARCHIVE ON 10:21:09 Oct 18, 2026.
```

i.e. **the injected banner embeds the fetch time**, so its length varies by a few bytes
per fetch (my two `--compressed` samples differ from the no-compression sample only in
that banner span, first differing at byte offset 127,170 of 127,638). Title, cited
chapter links and structure are identical in all samples. **Recommendation:** cite the
snapshot by date/id and content markers (or a digest of the copy actually used) rather
than a byte count that a replay cannot hold constant. The sibling C seat
(`.scratch/r18c09/probe-run1.log`, 10:23Z) independently measured 127,638 as well.

## 2. `polynesia-navigation.md` — never-swept sweep + 9 moved-locator re-pins (map idx 78)

Patch row claims: `distinct_before` 26 (24 live, 2 bot-block, 0 hard-fail); 8 POLLEX
locators re-pinned `pollex.eva.mpg.de → pollex.org.nz`; 1 Wehe re-pin
`hilo.hawaii.edu/wehe → wehe.hilo.hawaii.edu`; receipt `civ/polynesia-navigation.md`.

| # | fixer claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | 26/26 URLs swept, 24 live, 2 blocked, 0 hard fail | my sweep of the entry: **26 URLs → 24 × 200, 2 × 403** (`royalsociety.org.nz/…mau-moko…`, `doi.org/10.1093/oso/9780190681685.001.0001`), 0 × 000 | exact |
| 2 | POLLEX host 301-moved; each new target 200 with entry title checked | old `pollex.eva.mpg.de/entry/moana/` follows to **`pollex.org.nz/entry/moana/`** (200, identical body to the new URL); all 8 new entries (`waka.a`, `folau`, `fetuqu`, `matagi`, `laa.1`, `moana`, `kau-waka`, `search/?query=moana`) → **200** | exact |
| 3 | Wehe 301-moved; new target 200 | `hilo.hawaii.edu/wehe/?q=kāpeʻa` → effective **`wehe.hilo.hawaii.edu/?q=kāpeʻa`**, **200, 117,921 B** | exact |
| 4 | 2 MUSE DOI links resolve to a verification interstitial (not breakage) | `doi.org/10.1353/ol.2011.0014` and `doi.org/10.1353/cp.2004.0026` → **200 with ~1,072 B interstitial bodies**, not article bodies | consistent |
| 5 | after-hash `a47639dc…bb5981`; before-hash `ff72bf11…d0c33f` | delivered sha256 → **identical**; `git show f30b6f8:…/polynesia-navigation.md` → **`ff72bf1143be58fb…`** | exact |

**Verdict: VERIFIED — tally and both redirect families reproduce exactly.**

## 3. `rapa-nui.md` — never-swept sweep, no replacement needed (map idx 79)

| # | fixer claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | 9/9 URLs swept two runs: 8 × 200 with content markers, 1 × 429 host-wide metmuseum bot wall | my sweep: **9 → 8 × 200, 1 × 429** (`www.metmuseum.org/essays/easter-island`) | exact |
| 2 | the 429 is host-wide, not rot (control probe also 429) | control `https://www.metmuseum.org/` → **429, 34,218 B** (same body class as the essay's 34,217 B) | exact |
| 3 | content checked via a 2025-05-15 Wayback snapshot; KW02 early-date caution kept open | neither claim is re-runnable from this seat without the fixer's snapshot URL; the entry line 6 records the method and keeps the caution — read as documentation | documented |
| 4 | after-hash `c893805a…fb2a0f57`; before-hash `e56906e8…3cc1ec` | delivered → **identical**; `git show f30b6f8:…` → **`e56906e8317ca9a9…`** | exact |

**Verdict: VERIFIED — status classes and the host-wide-wall control reproduce.**

## 4. `rome.md` — never-swept sweep, no replacement needed (map idx 80)

| # | fixer claim | my independent re-run | verdict |
|---|---|---|---|
| 1 | 12/12 URLs swept (M04 method, balanced-paren extraction): 10 live, 2 cambridge.org 429s, 0 hard fails | my first pass (regex extraction) showed a 404 on `numismatics.org/ocre/id/ric.1(2` — **my own paren-truncation artifact**, the same class round-17's V02 seat recorded. Re-probed with the exact entry URL: **200** | artifact acknowledged |
| 2 | OCRE record live | `https://numismatics.org/ocre/id/ric.1(2).aug.206` → **200, 80,524 B**; negative control `…ric.1(2).aug.99999` → **404** (so the 200 is a real record, not a catch-all) | exact |
| 3 | 2 cambridge.org host rate-blocks with content verified via Crossref DOI records | my sweep: `doi.org/10.1017/CBO9780511843433` and `cambridge.org/core/…whats-in-a-name…` → **429, 1,302 B each** (Cloudflare-type challenge bodies) | exact |
| 4 | 10 live rows include the assets.cambridge.org frontmatter PDFs and the Thayer/Latin texts | my sweep: both frontmatter PDFs 200 (731,447 / 153,511 B) and all five penelope/latinlibrary pages 200 | exact |
| 5 | after-hash `0b29e05c…cfe68c`; before-hash `f0b2747c…1637fb` | delivered → **identical**; `git show f30b6f8:…/rome.md` → **`f0b2747c…`** | exact |

**Verdict: VERIFIED — 12/12 classes reproduce once the paren artifact is corrected;
the correction is recorded here rather than silently.**

## 5. Findings carried to the parent

- **F-C05-1** — Wayback replay byte-count variance (avesta fallback 127,638/127,640 vs
  receipt 127,643; mechanism = banner timestamp) — §1. Suggest the map row cite the
  snapshot id + content markers, not a byte count.
- **F-C05-2 (informational)** — rome's OCRE link is paren-bearing
  (`ric.1(2).aug.206`): any sweep whose extractor stops at `)` will record a false 404.
  Both round-17's V02 seat and this seat hit it. A map builder should carry the
  balanced-paren extraction note into the counting method.
- **F-C05-3 (informational)** — the persia receipt's "9/9 failed samples" for the
  avesta primary and the entry's willingness to keep the primary both reproduce; the
  primary is *dated-expired*, so the row's status should stay "live-with-fallback at
  this date", not "dead".

## 6. Compliance

Writes: **this file only**, plus gitignored scratch under `.scratch/r18c03/`
(`sweep.json`, `probe2.py`/`probe3.py` and their JSON, `bodies/**`; all scratch bytes
confined to `.scratch/` — `export TMPDIR=$PWD/.scratch` for the scripted passes, ad-hoc
fetches written directly into `.scratch/r18c03/bodies/`). No corpus entry, receipt,
map, tool or earlier-round byte was edited anywhere in this seat's work; no git
mutation; no commit; no writes outside the lane repo. Sibling scratch cited only as
cross-reference.
