# R17-V03/V04 — never-swept sweep verification + map-update check (round-17 claim C)

- Seat: **CIV R17-V03/V04** (round-17 C-verifiers 3–4; assignment: “the never-swept
  sweep verification; map-update check: propose the exact round-16 map row updates
  (stale->current transitions) as a JSON patch file
  `reports/round-17/civ/map-patch.json`”).
- Date: 2026-10-18. Verification window ~09:16–09:33Z (all stamps UTC unless marked).
  Lane root: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; reference revision
  `9b49a4a` (round-17 declare); declared baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`.
- Write surface: **this file + `reports/round-17/civ/map-patch.json`** (plus
  gitignored scratch `.scratch/r17-v34/`, `TMPDIR=$PWD/.scratch` before every
  scratch-writing command). Zero corpus bytes written by this seat; zero commits;
  no filed round-8…16 artifact modified (`reports/round-16/civ-map.json` is read
  only — the patch is a proposal file, not an edit).
- **NON-CANON.** Verification evidence only: no canon, rank, rights/clearance or
  freshness-axis ruling is made or implied. “Verified” below means *the fixer’s
  dated, command-carried claims reproduce against this seat’s independent runs* —
  not that the cited scholarship is current or correct.
- Freshness pause: this is a coverage receipt (claim C supplies dated URL-status
  receipts); no source-freshness axis-move is claimed.

## 1. Objects verified

| object | scope |
|---|---|
| the 7 never-swept entries | `persia-sasanian, polynesia-navigation, rapa-nui, rome, ryukyu, scythian-saka, siam-thai` — round-16 map rows 77–83 (1-based), **94 baseline distinct URLs** (9+26+9+12+12+12+14) |
| their round-17 receipts | `reports/round-17/civ/{persia-sasanian,polynesia-navigation,rapa-nui,sed77,sed78,sed79,sed80}.md` |
| the map-update object | all **12** stale-documented rows of `reports/round-16/civ-map.json` (sha256 `07cabb69b4a41c51b74767212a07ba4ffae3c09ef8c2571abd954b37342cb943`, filed, unmodified) |
| cross-check objects | the 5 fixed-type receipts (`inuit, maya-classic, mesoamerica, mongol, muisca`) — light battery here, deep verification owned by R17-V01/V02 |

Pre-fix state was captured before any fixer edit landed: URL sets extracted from
`git show HEAD:<entry>` into `.scratch/r17-v34/baseline-urls.json` (94 never-swept
+ 93 fixed-type URLs); the 12 baseline sha256s were independently snapshotted by
the sibling verifier seat at `.scratch/verify-baseline/sha256-baseline.txt`
(re-hashed against this seat’s `git show` — agreement).

## 2. Independent sweep of the 94 never-swept URLs (this seat)

Method = the filed M04 house method (`reports/round-8/metadata/m04-civ-58-76.md`
§3): `curl -sS -o /dev/null -w '%{http_code} %{url_effective} %{content_type}
%{size_download} %{time_total}' -L --max-time 15 -A
'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)'`, one retry on `000`,
6 concurrent (reduced from M04’s 16 because 11 sibling fixers swept concurrently).
Driver: `.scratch/r17-v34/independent-sweep.py`; raw JSON
`.scratch/r17-v34/independent-sweep.json` (2026-10-18T09:16:58Z).

| entry | URLs | live | bot-blocked (403/429) | hard-fail (000) | fixer receipt tally | agreement |
|---|---|---|---|---|---|---|
| persia-sasanian | 9 | 6 | 2 | 1 (avesta.org TLS) | 6 live / 2 blocked / 1 × 000 | 9/9 |
| polynesia-navigation | 26 | 24 | 2 | 0 | 24 live / 2 × 403 | 26/26 |
| rapa-nui | 9 | 8 | 1 | 0 | 8 live / 1 × 429 | 9/9 |
| rome | 12 | 10 | 2 | 0 | 10 live / 2 × 429 | 12/12 † |
| ryukyu | 12 | 11 | 1 | 0 | 11 live / 1 × 403 | 12/12 |
| scythian-saka | 12 | 11 | 1 | 0 | 11 live / 1 × 403 | 12/12 |
| siam-thai | 14 | 12 | 2 | 0 | 12 live / 2 × 403 | 14/14 |
| **total** | **94** | **82** | **11** | **1** | — | **94/94** |

† rome: this seat’s naive URL regex truncated the paren-containing OCRE id at the
first `)` (stored `…/ric.1(2` → 404 artifact). Corrected by balanced-paren
extraction (the fixer’s method) and re-probed directly by this seat:
`https://numismatics.org/ocre/id/ric.1(2).aug.206` → **200, 80524 B** (×2, plus
one 45 s timeout — the host is slow/flaky; see F-V34-1). All other 93 rows needed
no correction.

Per-URL comparison against each fixer’s own sweep (`.scratch/r17-v34/compare.py`,
`.scratch/r17-v34/compare.json`): **93/93 comparable rows agree, 0 unexplained
divergences** (codes compared exactly; {403,429,000} treated as the same
bot-wall/transient class, and none needed that leniency except the single
avesta `000` which both sweeps independently produced).

## 3. Receipt battery (the 7 never-swept receipts)

For each receipt: (a) exists, dated 2026-10-18, command-carried; (b) the receipt’s
swept URL set equals the baseline set; (c) per-URL codes reproduce my sweep;
(d) the claimed before/after sha256 chain reproduces on delivered bytes; (e) the
corpus edit carries the round-16 reason trail; (f) gate clean; (g) every
old→new locator re-probed by this seat.

| receipt | swept set == baseline | codes reproduce | delivered sha256 == receipt after-hash | edit | gate | new locators re-probed |
|---|---|---|---|---|---|---|
| `persia-sasanian.md` | 9/9 | 9/9 | `20e7513e…40ca7e2e` ✓ | 4 lines | findings=0 | Wayback avesta copy 200/127635 B; Silk Road 14 PDF 200/948943 B |
| `polynesia-navigation.md` | 26/26 | 26/26 | `a47639dc…6bb5981` ✓ | 3 lines | findings=0 | pollex.org.nz/moana 200; wehe.hilo.hawaii.edu 200 |
| `rapa-nui.md` | 9/9 (2 runs) | 9/9 | `c893805a…fb2a0f57` ✓ | 1 line | findings=0 | none (no replacement) |
| `sed77.md` (rome) | 12/12 | 12/12 | `0b29e05c…bcfe68c` ✓ | 1 line | findings=0 | none; both 429 DOIs re-verified by this seat via Crossref CSL-JSON (Adams 2013; Salway 1994 JRS 84:124–145) |
| `sed78.md` (ryukyu) | 12/12 | 12/12 | `424fcbb5…819afa5` ✓ | 1 line | findings=0 | none (no replacement) |
| `sed79.md` (scythian-saka) | 12/12 | 12/12 | `cb3a6428…b3ab5c51` ✓ | 2 lines | findings=0 | Leiden handle/1887/16379 200/8911 B |
| `sed80.md` (siam-thai) | 14/14 | 14/14 | `8bef2a5b…7cb6c733` ✓ | 4 lines | findings=0 | theculturalatlas.org 200/118615 B; cdlib public/book 200/1657019 B |

Body-digest reproduction: rapa-nui’s 8 fetched bodies (`.scratch/r17c08/body/`),
rome’s 12 bodies (`.scratch/r17c09/`), persia-sasanian’s 4 PDFs
(`.scratch/r17c06/`), scythian’s bodies (`.scratch/r17c11/body/`) — every sha256
claimed in the receipts recomputes exactly. Gate re-run on all 7 together:
`python3 tools/gates/provenance-audit.py <7 paths>` →
`files=7 marks=3 mark-lines=3 findings=0 blocked=0`, exit 0 (marks: persia 1,
rapa-nui 2 — unchanged from the round-16 shard inventory).

Delivered-hash re-check at patch build (2026-10-18T09:31Z), all 12 entries:
`inuit 52c5a11b`, `maya-classic d9608d84`, `mesoamerica d04d8913`,
`mongol e60b3903`, `muisca 417b7086`, `persia-sasanian 20e7513e`,
`polynesia a47639dc`, `rapa-nui c893805a`, `rome 0b29e05c`, `ryukyu 424fcbb5`,
`scythian cb3a6428`, `siam 8bef2a5b` — each equals its receipt’s after-hash.

## 4. Findings (reported, not absorbed)

- **F-V34-1 — paren-URL extraction artifact (informational).** Naive `https?://`
  regexes truncate `https://numismatics.org/ocre/id/ric.1(2).aug.206` at the
  first `)`, yielding a 404 on a live URL. It affected this seat’s inventory and
  the sibling verifier’s (`.scratch/v01/sweep12.json` rome shows the same 404:1);
  the fixer’s balanced-paren extractor is correct, and a direct re-probe by this
  seat returns 200 (×2, one 45 s timeout — slow host). No receipt claim depends on
  the truncated form.
- **F-V34-2 — receipt byte columns vs body digests (informational; matches
  V01’s note).** `sed77`’s byte column records `size_download` under
  `--compressed` (wire size; e.g. OCRE 11,046 B) while the stored body is the
  decompressed 80,524 B; the **body sha256 binds exactly** in all 12 rows.
  Re-runners should compare digests, not raw byte counts.
- **F-V34-3 — mid-run receipt/hash revisions (process observation).** `sed77`
  (rome) and `sed80` (siam-thai) were re-written after their entries’ final edits;
  in both cases the delivered bytes match the **final** receipt text (this seat
  re-hashed after the revisions; the earlier drafts’ hashes are superseded, and
  V01 recorded the same resolution for sed77). No open inconsistency remains.
- **F-V34-4 — round-16 map reason-text defect (carried, not rewritten).** All 7
  never-swept rows’ reason text says “its 94 distinct cited URLs”; 94 is the
  7-entry group total (`reports/round-16/civ/072-083.md` §3), not per-entry.
  Recorded independently by `sed78` §0 and `polynesia-navigation.md` §1; filed
  round-16 bytes are not rewritten, and the patch’s `from_` rows preserve the
  text verbatim.
- **F-V34-5 — status labeling (`current` vs `stale-fixed`).** Seats filed
  `stale-fixed` for 11 rows and `current` for rome (its receipt carries
  `status_after=current`, `disposition=stale-fixed`). The round-16 map’s `current`
  definition (“cited source re-fetched … this round, with date+command”) is now
  satisfied by every row, and round-16 labeled its one corrected entry
  (`africa-primary-sources`) `current`. The patch preserves the seats’ filed
  statuses and carries a `label_policy_note` so the parent/map-scribe can
  normalize if the map is to record terminal state. Claim C’s stale-count drop
  holds under either labeling (12 → 0).
- **F-V34-6 — validator fixed/attempted classification (informational; same as
  V01’s F-V01-2).** `reports/round-17/validation.json` classifies 5 entries
  `attempted` (they keep the old URL inside the old→new trail text) and 7
  `fixed`; claim C passes (`failures: []`). Underlying facts verified above.
- **F-V34-7 — the single hard failure.** `https://www.avesta.org/mp/grb.htm`
  returns `000` (curl error 60: expired TLS certificate; reproducible 9/9 in the
  fixer’s samples, 2/2 in this seat’s). Disposition: primary kept (canonical
  citation), dated Wayback fallback added to the entry, content-checked
  (snapshot 200, links the cited chapters). This is the only non-bot-wall
  external failure in the 94; it is *documented with a fallback*, not silently
  absorbed, and no rights/clearance claim is made about the archived copy.

## 5. Map-update check — `reports/round-17/civ/map-patch.json`

Built by `.scratch/r17-v34/build-map-patch.py --write` (12/12 rows; build-time
assertions: `from_` values byte-equal to the filed round-16 rows; evidence paths
exist; delivered sha256 == each row’s claimed after-hash). The patch:

- targets the **filed** round-16 map (pinned sha256) and does not modify it;
- carries 12 row replacements, each with `from_` (exact filed values), `to`
  (proposed round-17 row: status, verified_at, command, evidence_path, reason),
  `disposition` (sweep tallies, replacements, entry edit, digest chain) and
  `verification` (this seat’s checks);
- summary: **stale-documented 12 → 0** (11 × `stale-fixed` + 1 × `current`;
  `rows_pending: 0`); never-swept group: 94/94 swept, independent agreement
  94/94 (81/81 directly comparable + the OCRE paren correction);
- `label_policy_note` (F-V34-5) and `limits` (point-in-time; bot-wall
  classification per M04; light vs deep verification split for the 5 fixed-type
  rows).

Re-run to reproduce: `export TMPDIR=$PWD/.scratch && python3
.scratch/r17-v34/build-map-patch.py` (prints `rows patched: 12/12`).

**Patch pin:** `reports/round-17/civ/map-patch.json` sha256
`79ceafabac9fd84d6bec5cb701e3d1791b075e5e1300d7164126e40f9876e77e` (2026-10-18
09:34Z, rebuilt after adding the sibling-verification block), independently
re-parsed and re-validated against the filed map and the delivered corpus bytes
(12/12 `from_` rows equal; evidence paths exist; delivered hashes match).

## 6. Cross-verification

- **R17-V01** (`reports/round-17/civ/verify-1.md`, group 1: inuit, maya-classic,
  mesoamerica, mongol, muisca, **persia-sasanian**): all six **VERIFIED**, with
  byte-exact hashes matching this seat’s re-hash; its F-V01-2/F-V01-3 and
  byte-count note agree with F-V34-2/F-V34-6/F-V34-3 here.
- **R17-V02** (`reports/round-17/civ/verify-2.md`, group 2: rapa-nui, rome,
  siam-thai, polynesia-navigation, ryukyu, scythian-saka — six of this seat’s
  seven never-swept entries): **all six VERIFIED** (every static check exact on
  polynesia/ryukyu/scythian; rome tallies/DOIs exact; rapa-nui static exact with
  dynamic-page hash variance noted as F-V02-2; siam-thai verified with the
  non-dispositional CDX-wording finding F-V01-1). V02’s F-V02-1 (rome
  `--compressed` byte column) and F-V02-3 (round-16 map reason “94” text) agree
  with this seat’s F-V34-2 and F-V34-4. The two independent verification chains
  (V02’s and this seat’s) therefore agree row-for-row on all six shared entries;
  persia-sasanian is jointly covered by V01 (verify-1.md) and this seat.
- Counting command on the settled tree at write time:
  `reports/round-17/validation.json` (validation seat, 06:30 local) shows claim C
  `failures: []`; this seat additionally ran `run-validation.py --check`
  (non-writing) at 09:32Z and recorded the output in
  `.scratch/r17-v34/validation-check.json`: **claim C passed, 0 failures**
  (fixed: inuit, maya-classic, mesoamerica-primary-sources, persia-sasanian,
  polynesia-navigation, scythian-saka, siam-thai; attempted: mongol, muisca,
  rapa-nui, rome, ryukyu — the F-V34-6 labeling). Claims D and O were still red
  at that instant (D4 artifacts and `tools/assemble-culture-d4.py` not yet
  landed — other seats’ in-flight work, outside this seat’s scope).

## 7. Limits

- Point-in-time: sweeps ran 2026-10-18 ~09:16–09:22Z during a live 64-worker
  wave; a single-day sweep cannot rule out intermittent failure (the receipts
  say so themselves; avesta’s TLS expiry is the counter-example that a sweep can
  only date, not fix).
- 403/429/202 outcomes are classified as bot walls/access outcomes per the M04
  precedent, not as link rot; the two MUSE DOIs resolve to verification
  interstitials for curl.
- Presence-level verification only (statuses, effective URLs, titles, keyword
  receipts, body digests). No passage-level scholarly re-inspection; no content
  accuracy, canon, or rights ruling.
- Scratch evidence under `.scratch/` is gitignored and may be pruned; the
  durable evidence is the digests, codes and commands carried in the receipts
  and in this file.
- The 5 fixed-type rows are verified **lightly** here (digest, edit shape, new
  locator liveness); their deep independent verification is R17-V01/V02’s, and
  the patch labels them as such.

## Appendix A — commands (verbatim, 2026-10-18)

```
# baseline snapshot (pre-fix)
python3 - <<'EOF'   # extract URLs from git show HEAD:<entry> -> .scratch/r17-v34/baseline-urls.json
EOF
sha256sum corpus/knowledge/civilizations/{persia-sasanian,polynesia-navigation,rapa-nui,rome,ryukyu,scythian-saka,siam-thai}.md

# independent sweep (94 URLs; M04 method; retry once on 000; 6 workers)
export TMPDIR=$PWD/.scratch && python3 .scratch/r17-v34/independent-sweep.py

# fixer-sweep comparison (93 comparable rows; rome OCRE handled separately)
python3 .scratch/r17-v34/compare.py

# receipt battery (per file): hash chain, diff shape, gate, body digests
sha256sum corpus/knowledge/civilizations/<entry>.md
git diff --numstat corpus/knowledge/civilizations/<entry>.md
python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/{persia-sasanian,polynesia-navigation,rapa-nui,rome,ryukyu,scythian-saka,siam-thai}.md
# body-digest reproduction: recompute sha256 of .scratch/r17c06|r17c08|r17c09|r17c11 bodies vs receipt tables

# replacement/fallback locator probes (this seat, M04 UA)
curl -sS -o /dev/null -w '%{http_code} %{size_download} %{content_type}\n' -L --max-time 25 \
  -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)' <new-url>   # x6 (see §3 table)

# Crossref content routes for the two rome 429s
curl -sS -L -H 'Accept: application/vnd.citationstyles.csl+json' https://doi.org/<doi>

# map patch (validates from_ vs filed map; asserts hashes; writes the patch)
export TMPDIR=$PWD/.scratch && python3 .scratch/r17-v34/build-map-patch.py --write

# counting command on the settled tree, non-writing
export TMPDIR=$PWD/.scratch && python3 reports/round-17/run-validation.py --check > .scratch/r17-v34/validation-check.json
```

— CIV R17-V03/V04, 2026-10-18. All artifacts NON-CANON. Fixer receipts and this
verification are lane evidence; promotion/acceptance is the parent’s.
