# R17-C04 — fixer: `mesoamerica-primary-sources.md` (3 hard-fail URLs + pin drift)

- seat: **R17-C04** (claim C fixer, round 17 — operator regimen loop 2 of 3, build 1 of 4; 64w `opencode-go/deepseek-v4.1-flash`); date 2026-10-18 (runs 09:15:39Z–09:23:29Z UTC, `date -u` stamps below).
- assignment (verbatim): "C R17-C04 (mesoamerica fixer): same protocol for mesoamerica-primary-sources.md's 3 hard-fail URLs + pin drift; reports/round-17/civ/mesoamerica.md."
- lane `kotodama-shokunin`; HEAD at run `9b49a4a` (sibling fixers' corpus edits present in the worktree, none touched by this seat); claims baseline `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`.
- write scope: **this file** + `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` (the only entry the assignment names) + gitignored scratch `.scratch/r17c04/` (`TMPDIR=$PWD/.scratch` set before every scratch write). No filed round-8–16 byte was edited; no git operation; all artifacts NON-CANON; no real-world rights/clearance ruling (none arises).
- tooling: `curl 8.22.0 … OpenSSL/3.6.4`, `python3 3.14.7`, `openssl` s_client, `pdftotext`/`pdfinfo`.

## 0. Object under fix, stamped

| object | sha256 | bytes | note |
|---|---|---|---|
| `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` **pre-edit** | `6d40a97d2b025fb43317ecd8477afc3082ab4a1e43efcf58ebf82c70b477bcb2` | 46,781 | equals the round-16 shard's claimed digest (`reports/round-16/civ/060-071.md:89`, `:120`) and `git show e1694ba:…` bytes (checked 2026-10-18) |
| same file **post-edit** | `d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530` | 49,538 | this seat's fix (§4); a future re-pin must copy these bytes |

## 1. The debt, verbatim with locations

- Round-16 map row 62 (`reports/round-16/civ-map.json`): `"status": "stale-documented"`, reason `"3 hard-fail 000 URLs + round-11 pin drift (r16 C06 in-repo verification) [evidence: reports/round-16/civ/060-071.md]"`.
- Round-16 shard `reports/round-16/civ/060-071.md:89`: "(a) 3 hard-fail (000) URLs from M §3: `florentinecodex.getty.edu/en/book/12/folio/19v`, `iifilologicas.unam.mx/…/totonicapan_simonetta2.pdf`, `liblilly.sitehost.iu.edu/etexts/nahuatl/index.shtml`; no re-attempt rounds 9–15 … (b) live-bytes drift vs round-11 pin (`6d40a97d…` vs `a916a4c2…`, `reports/round-11/depth/frozen-records.md:73`) — verdict unaffected per round-8 control C4; any future re-pin must copy current bytes".
- Origin receipt: `reports/round-8/metadata/m04-civ-58-76.md:83–85` (the 3 × `000` rows, retried once) and `:62` (`| mesoamerica-primary-sources.md | 46 | 35 | 11 |`).

## 2. Method and controls (2026-10-18)

Strict sweep (the round-8 form, so results are comparable):

```
for u in <urls>; do curl -sS -o /dev/null -w '%{http_code} %{size_download} %{content_type}' \
  -L --max-time 25 -A 'Mozilla/5.0 (X11; Linux x86_64) kotodama-r17-c04/1.0' "$u"; done
```

Controls used to separate **TLS-verification failure** from **content failure**:

1. `-k` re-run (verification relaxed) — shows what the server actually serves.
2. `openssl s_client -connect host:443 -servername host -showcerts` + `Verify return code` — identifies the failure class (chain vs expiry vs hostname).
3. Chain-valid sibling pages where they exist (Getty project page; ScholarWorks; Wayback) as positive controls.
4. Prior-round sweep for re-attempts (negative-claim control, §5.1).

Round-16's own shard made zero fetches (freshness pause then in force); this seat's claim explicitly authorises the re-attempt, so live fetches are the evidence.

## 3. Results and dispositions

| # | URL | strict | `-k` content | TLS diagnosis | disposition |
|---|---|---|---|---|---|
| 1 | `https://florentinecodex.getty.edu/en/book/12/folio/19v` | `000 0` | **200, 267,502 B, text/html**; title `Book 12 Folio 19v\| Digital Florentine Codex`; body markers `19v`×19, `Book 12`×16, `Terraciano`×8 | leaf `CN=florentinecodex.getty.edu`, issuer `InCommon Intermediate CA - OVG2C` **not sent**; `Verify return code: 21 (unable to verify the first certificate)` | **retained; not dead** — content live, strict-client failure is an incomplete TLS chain; caveat recorded in-entry ([FC]) |
| 2 | `https://iifilologicas.unam.mx/estmesoam/uploads/Vol%C3%BAmenes/Volumen%206/totonicapan_simonetta2.pdf` | `000 0` | **200, 3,499,309 B, application/pdf**; `pdfinfo`: 16 pp., EPSON Scan, created 2013-04-02 | leaf issuer `GlobalSign RSA OV SSL CA 2018` **not sent**; `Verify return code: 21`; SANs cover `iifilologicas.unam.mx` **and** `www.iifilologicas.unam.mx` (hostname fine) | **retained; not dead** — same incomplete-chain class; caveat recorded in-entry ([HIG]) |
| 3 | `https://liblilly.sitehost.iu.edu/etexts/nahuatl/index.shtml` | `000 0` | **404, 146 B**, nginx body (`<title>404 Not Found</title>`) | certificate `CN=*.bio.indiana.edu` — hostname mismatch (`SSL: no alternative certificate subject name matches`) | **real rot → replaced** with two content-verified locators (§3.3); old URL kept as plain text for the old→new trail |

Positive controls: `https://www.getty.edu/projects/florentine-codex/` strict **200, 3,162,177 B** (chain valid); `https://www.iifilologicas.unam.mx/estmesoam/` `-k` 200, 12,579 B (same host, same caveat).

### 3.3 Replacement for the dead Lilly locator (content-verified 2026-10-18)

- **Live published version**: `https://scholarworks.iu.edu/journals/index.php/bookman/article/view/3788` strict **200, 19,081 B** (citation metadata: author `John Frederick Schwaller`, title, *The Indiana University Bookman*, firstpage 69, lastpage 88); PDF galley `https://scholarworks.iu.edu/journals/index.php/bookman/article/download/3788/3500` strict **200, 5,388,824 B, application/pdf**. Content check: `pdftotext` (38,549 chars) contains `By JoHN FREDERICK ScHWALLER`, entry 2 `… en la lengua castellana y mexicana. [Mexico: Juan Pablos, 1555]` and `The Vocabulario of 1555 was revised, augmented, and reprinted … Mexico: Antonio d e Spinosa, 1571`.
- **Archived machine-readable transcription** (the exact object the entry cited): Wayback raw snapshot `https://web.archive.org/web/20210227003441id_/https://liblilly.sitehost.iu.edu/etexts/nahuatl/index.shtml` strict **200, 130,398 B**, sha256 `27d6a210bfc3a88da9015e52537c51f6b529411b361b3f333b3b5120cbae09ae`; title `A Catalogue of Pre-1840 Nahuatl Works Held by The Lilly Library: a machine-readable transcription`; entry `2.` re-checked (Molina, Pablos 1555, Spinosa 1571). Wayback CDX record for the original URL: 200 snapshot `20210227003441`, digest `4AUXOKXXL3RVLQ5K7XUZNAKEXA5JVJHV`.
- Dead-end control recorded so it is not mistaken for the replacement: `http(s)://www.indiana.edu/~liblilly/etexts/nahuatl/` → **200, 318,019 B** but it is IU's catch-all homepage (`Indiana University Bloomington | Academics, research, and impact`), not the transcription.

### 3.4 Pin drift — explained, re-based

```
sha256sum tools/gates/frozen/round-3/inputs/corpus/knowledge/civilizations/mesoamerica-primary-sources.md \
          tools/gates/frozen/round-3/attempt-1/inputs/corpus/knowledge/civilizations/mesoamerica-primary-sources.md
→ a916a4c2dd30d1a81415ddbcf7df1bb2474cb4caf808b898481d18ff5d846c7c  (both, 32,633 B)
git show c610e0a:corpus/knowledge/civilizations/mesoamerica-primary-sources.md | sha256sum
→ a916a4c2…  (round-3 commit state)
git show e1694ba:corpus/knowledge/civilizations/mesoamerica-primary-sources.md | sha256sum
→ 6d40a97d…  (46,781 B; round-4 revision 1.1, unchanged by round-8 admit)
```

The round-11 pin `a916a4c2…` (`reports/round-11/depth/frozen-records.md:73`, "`input_sha256` … `a916a4c2dd30d1a8…` (mesoamerica, 32633 B)") is **byte-identical to the frozen round-3 gate-snapshot input**, i.e. the pre-round-4 bytes; the live corpus file had already moved to revision 1.1 in round 4. The "drift" is therefore pin-of-snapshot vs live-file, not corpus drift this round; verdict unaffected (round-8 control C4: the replay reads the frozen input only). **Re-pin basis for any future re-pin: the post-edit bytes `d04d8913…` (§0) — not the round-11 value and not the pre-edit value.**

## 4. Entry edits made (only the assignment-named entry)

`corpus/knowledge/civilizations/mesoamerica-primary-sources.md`, all edits carry the round-16 reason trail (`reports/round-16/civ/060-071.md`):

| line | change |
|---|---|
| 2 | `revision: 1.1` → **`1.2 — 2026-10-18, round-17 locator re-attempt (round-16 map row 62 debt: 3 hard-fail 000 URLs + round-11 pin drift …)`**, original 1.1 text retained after it |
| 9 | [FC] appended the folio-URL re-attempt: content 200 (267,502 B; page title) + incomplete-TLS-chain caveat + receipt pointer |
| 30 | [HIG] appended the PDF re-attempt: content 200 (3,499,309 B, 16 pp.) + chain caveat + SAN fact |
| 33 | [MOL] locator replaced: dead transcription URL kept as plain text, replaced by ScholarWorks article + PDF + Wayback raw snapshot, with digests and re-checked entry-2 content |
| 38 | `verified-at` appended: round-17 re-attempt summary (2 live-with-caveat / 1 replaced) + pin re-base + receipt pointer |
| 175 | known-open-items appended: the two incomplete-TLS-chain hosts and the [MOL] replacement note |

Post-edit counts (2026-10-18T09:23Z): distinct URLs **46 → 49** (`grep -oE 'https?://[^ )">]+' … | sort -u | wc -l`), header fields 5/5 (`topic`/`sources`/`couples`/`verified-at`/`recheck` = 1 each), `to-verify` lines **12 (unchanged)**; bytes 46,781 → 49,538. The +3 net URLs are the two new [MOL] locators and the archived-snapshot URL.

## 5. Negative claims and their sweeps

1. **"No re-attempt of these URLs existed in rounds 9–16."** Sweep (2026-10-18): `grep -rn -E 'florentinecodex\.getty|iifilologicas|liblilly' reports/round-9 … reports/round-16` → hits only in `reports/round-16/civ/060-071.md` (lines 76, 89, 120); rounds 9–15 zero hits. Reproduces the round-16 shard's own claim.
2. **"The two strict failures are incomplete-chain artifacts, not rot, expiry, or hostname mismatch."** Evidence: `Verify return code: 21` + chain dumps show the intermediate absent in both cases; iif SANs include both hostnames; both serve 200 under `-k`; chain-valid controls on sibling paths behave normally. Consequence: these two URLs are live-with-caveat, and the caveat is server-side TLS configuration, so it can be dropped at a future sweep if the hosts fix their chains.
3. **"The Lilly URL is dead, not bot-walled."** Evidence: `-k` 404 nginx body (146 B); cert hostname mismatch on the legacy `sitehost` vhost; a 2021 Wayback 200 snapshot exists. (Contrast: the round-8 sweep's 403/429 class was explicitly *not* treated as rot; this one is a 404 with a live replacement.)

## 6. What this file does not do

- No independent verification: this is fixer evidence; the verifier seat re-runs the claim's checks. The round-17 counting command appeared mid-run (sibling build) and was executed read-only at **2026-10-18T09:25:06Z**: `python3 reports/round-17/run-validation.py` → **claim C: PASS** (claims D/O FAIL — their artifacts are other seats' and not yet built); its `validation.json` records this entry as `fixed`, baseline `6d40a97d…` → current `d04d8913…` (`claims/C/measurement/corpus_edits[61]`). Note: the validator's fragment-chooser picked `reports/round-17/civ/maya-classic.md` for this entry on a rank tie (both fragments classify `fixed`); this fragment is listed among the naming fragments.
- The old Lilly URL stays in the entry as the documented old→new trail and will keep failing a strict sweep; a future map must classify it by the entry note, not by its bare status code.
- No canon, no clearance ruling, no S18/SN16 or other open-item re-inspection; no other entry touched; no git commit.

## 7. Map-scribe input

```json
{
  "file": "mesoamerica-primary-sources.md",
  "path": "corpus/knowledge/civilizations/mesoamerica-primary-sources.md",
  "status": "stale-fixed",
  "verified_at": "2026-10-18",
  "old_url": "https://liblilly.sitehost.iu.edu/etexts/nahuatl/index.shtml",
  "new_url": "https://scholarworks.iu.edu/journals/index.php/bookman/article/view/3788",
  "old_to_new": "404 dead -> live published version (ScholarWorks; PDF download/3788/3500) + archived machine-readable transcription (web.archive.org/web/20210227003441id_/...)",
  "sha256_before": "6d40a97d2b025fb43317ecd8477afc3082ab4a1e43efcf58ebf82c70b477bcb2",
  "sha256_after": "d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530",
  "reason": "round-16 map row 62 debt re-attempted live 2026-10-18 (curl 8.22.0): 2 of 3 hard-fail URLs serve content (getty folio 200/267,502 B; iif PDF 200/3,499,309 B) and fail strict verification only because the hosts send incomplete TLS chains (openssl Verify return code 21; intermediates not sent); 1 URL (liblilly transcription) is a genuine 404 and was replaced with two content-verified locators; pin drift re-based: round-11 pin a916a4c2 equals the frozen round-3 snapshot input (32,633 B), live pre-edit bytes 6d40a97d (46,781 B) were the round-4 revision; entry edits carry the round-16 reason trail",
  "urls_retained_with_caveat": [
    "https://florentinecodex.getty.edu/en/book/12/folio/19v (content live; incomplete chain: InCommon Intermediate CA - OVG2C not sent)",
    "https://iifilologicas.unam.mx/estmesoam/uploads/Vol%C3%BAmenes/Volumen%206/totonicapan_simonetta2.pdf (content live; incomplete chain: GlobalSign RSA OV SSL CA 2018 not sent)"
  ],
  "pin_repin_basis": "d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530",
  "evidence": ["reports/round-17/civ/mesoamerica.md"],
  "reason_trail": ["reports/round-16/civ/060-071.md", "reports/round-16/civ-map.json", "reports/round-8/metadata/m04-civ-58-76.md", "reports/round-11/depth/frozen-records.md"],
  "limits": "getty/iif content verified under relaxed TLS only (server-side incomplete chains); old liblilly URL retained as trail and still fails strict sweeps; presence-level verification, no full-text reading of the getty folio beyond title/markers"
}
```

```json
{
  "round": 17, "claim": "C", "seat": "R17-C04", "date": "2026-10-18",
  "entry": "corpus/knowledge/civilizations/mesoamerica-primary-sources.md",
  "pre_edit_sha256": "6d40a97d2b025fb43317ecd8477afc3082ab4a1e43efcf58ebf82c70b477bcb2",
  "post_edit_sha256": "d04d8913e704961533d123857d87c93d8cfc25b89c854b1f6c3f5bcf1d0db530",
  "urls": {"hard_fail_before": 3, "live_with_tls_caveat": 2, "replaced": 1, "still_dead_and_retained_as_trail": 1},
  "distinct_urls": {"before": 46, "after": 49},
  "pin": {"round11_pin": "a916a4c2dd30d1a8", "pin_equals": "frozen round-3 snapshot input (32,633 B)", "live_pre_edit": "6d40a97d2b02", "repin_basis": "post-edit d04d8913e704"},
  "receipts": ["reports/round-16/civ/060-071.md", "reports/round-8/metadata/m04-civ-58-76.md", "reports/round-11/depth/frozen-records.md"],
  "status": "stale-fixed (2 locators retained with corrected status + caveat, 1 replaced old->new, pin re-based)",
  "canon": false
}
```
