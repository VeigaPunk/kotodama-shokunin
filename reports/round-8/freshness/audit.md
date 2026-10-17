# Round-8 freshness receipts — X02 audit

- Auditor: X02 scribe (F-receipts auditor), author-side. **Not an independent promotion verifier.**
- Audit window: 2026-10-17T17:12–17:31 local (-03:00); retrieval re-checks performed live in that window.
- Scope: `reports/round-8/freshness/R8-F01..R8-F15-receipt.json`, plus `reconciliation.json` (checked because the F claim names it).
- Counting command for this audit's receipt count (run 2026-10-17):
  `ls reports/round-8/freshness/R8-F*-receipt.json | wc -l` → **15 at 17:28:27** (poll every 60 s from 17:13: 2 at 17:17, 6 at 17:18, 8 at 17:19, 13 at 17:22, 14 at 17:23–17:27, 15 at 17:28:27).
- Method: (a) structural scan of every receipt (URL, accessed-at, locator, excerpt, support-scope fields);
  (b) independent re-fetch of the cited sources for every receipt, then char-normalized quote matching
  (NFKC, quote/dash folding, whitespace collapse) against the passage I retrieved;
  (c) sha256 comparison where a receipt claims an artifact hash; (d) accessed-at plausibility vs file mtime.

## 1. Verdict summary (15/15 receipts landed)

| Receipt | Prior row | Spot-check I ran (my own fetch) | Quote located as claimed | Verdict |
|---|---|---|---|---|
| R8-F01 | R6-02-A | Wikipedia "Sumerian language" live fetch | Yes — lead ¶ verbatim modulo omitted ref marker `[5]` | pass |
| R8-F02 | R6-02-B | FIT "Kaunakes" page; Louvre AO 17551 notice; (Perseus LSJ — my fetch got 503) | Yes — FIT quotes 2/2 verbatim; Louvre notice carries "jupe de type kaunakès", "Dynastique archaïque IIIB", "Ebih-Il"; its entry hash matches live | pass |
| R8-F03 | R6-05-B | Wikipedia "Yazılıkaya" + UZH IDD PDF (`e_idd_anatolia_north_syria.pdf`) | Yes — Wikipedia sentence verbatim; IDD quote at txt lines 245–246; **IDD PDF/txt sha256 match the receipt exactly** | pass (strongest) |
| R8-F04 | R6-07-A | Wikipedia "Melqart", WiBiLex "Melqart" (FetchURL), Euphrosyne 45/2017 PDF (RODIN) | Yes — all three verbatim (WiBiLex via FetchURL; plain curl is 403, bot wall) | pass |
| R8-F05 | R6-04-A | Cambridge Apollo deposit PDFs (Salgarella; Steele–Meissner) | Yes — **sha256 matches receipt exactly** (`f2451475…`, `1d9818c3…`); quotes at their exact cited lines 534 and 699 | pass (strongest) |
| R8-F06 | R6-05-A | UT Austin Hittite Online Lesson 2 | Yes — 3/3 quotes verbatim | pass |
| R8-F07 | R6-06-A | Columbia AFE oracle-bone page | Yes — 3/3 quotes verbatim; main-leg passages are identical to round 6 (receipt discloses this; round-8 value = fresh 200) | pass with note |
| R8-F08 | R6-06-B | zh.wikisource 周禮/春官宗伯 | Yes — both Chinese quotes verbatim on a fresh fetch | pass |
| R8-F09 | R6-08-A | he.wikisource Sotah 7:6 + Jewish Encyclopedia "Names of God" | Yes — pointed sentence, Rambam and Bartenura lines present in raw HTML; 4/4 JE quotes verbatim | pass |
| R8-F10 | R6-08-B | mechon-mamre Exodus 28 | Yes — 4/4 verse quotes verbatim | pass |
| R8-F11 | R6-09-A | Wayback capture `20250922051004id_` of the Stolper–Tavernier PDF | Yes — **sha256 matches receipt exactly**; quote at txt lines 243–246, printed p. 9 (parent's page-9 correction holds) | pass (strongest) |
| R8-F12 | R6-09-B | Both Iranica Wayback snapshots (fravasi 20261009104155; ahura-mazda 20251119090540) | Yes — both quoted passages verbatim (entity-decoded); "Vol. I, Fasc. 7, pp. 684–687" header present | pass |
| R8-F13 | R6-10-A | PMC8462907 (Posth et al. 2021) | Yes — 3/3 quotes verbatim | pass |
| R8-F14 | R6-12-A | Ityopis Rilly 2011 PDF (re-download) | Yes — **sha256 matches receipt exactly** (`c718e208…`); 3/3 quotes verbatim | pass (strongest) |
| R8-F15 | R6-12-B | Thayer Strabo 17.1.54 | Yes — 2/2 quotes verbatim (source's "fugitive" singular matches, as the receipt says) | pass |

All 15 receipts carry: source URL, accessed-at date, a quoted passage with a named location, and a
support-scope statement; each documents its access failures with the attempted command and status
(F09 has no failure field because none occurred in its record; all others carry one, including F02 and F03).

## 2. Spot-check sample and coverage

- Spot-checks performed: **15 of 15 receipts** (target was ≥5).
- Byte-level corroborations (my download vs receipt's claimed hash): **6** — F03 (IDD PDF and its text), F05 (×2 artifacts), F11, F14.
- Exact extraction-line agreement with a receipt's own locator: **3** where both sides used `pdftotext -layout` —
  F05 (lines 534 and 699), F11 (lines 243–246), F03 (IDD lines 245–246; also 1448-line count match).
  F14's quotes are on the pages its locators name (abstract p. 1, p. 3, p. 5), but our extraction line numbers
  differ by invocation, so line equality is not claimed there.
- Quotes that did **not** initially match and why: F01 (`[5]` citation marker omitted — benign, disclosed practice);
  F09/F12 (`&scaron;`/gershayim entity and tag-splitting artifacts — matched after entity-aware normalization).
  One non-match was my own access failure: Perseus LSJ (F02-P2) returned HTTP 503 to my curl; the receipt's
  quotation is plausible but I did not re-verify that leg. No case was found where the quoted passage failed to
  support the scope the receipt claims for it.

## 3. Findings

**3.1 Entry-hash and line-locator staleness from the concurrent metadata sweep (affects 12 of 15 receipts).**
The round-8 metadata sweep (`targets.json.metadata_sweep`) edited all nine entry files during this same window
(`git diff --numstat`, 2026-10-17): frontmatter insertions of +1 to +3 lines per file — nubia-kush +3,
anatolia-hittite +3, mesopotamia-sumer-akkad +3, aegean-minoan-mycenaean +3, persia-achaemenid +3, etruria +3,
levant-canaan-phoenician +2, israel-ancient-hebrew +2, china-shang-zhou +1. Entry mtimes: 17:18:22–17:25:27.
Consequences, verified empirically:

- Receipts' `entry_sha256*` values are snapshots of the entry at the shard's own measurement time. Live matches:
  F02 (`bf6c92f9…` = live, post-sweep), F05 (`a9b16ab15d…` = live), F08 (`entry_sha256_live_at_handoff` `334f935b…` = live).
  The other 12 receipts' hashes no longer equal the live files (`sha256sum corpus/knowledge/civilizations/<entry>.md`, 2026-10-17).
- Line locators drift by the file's insertion count. Verified: F01's "line 36 Contact ecology" row is now line 39 (+3);
  F04's "line 76" mlqrt claim is now line 78 (+2); F07's cited oracle-corpus line is now line 50 (+1).
  F02's own `entry_locator_drift` block independently records the same effect for its costume table (+3, ledger 139→142 etc.).
- F14 and F15 additionally assert `entry_unchanged_since_round6: true`; that was true at their measurement time
  but **already stale when the receipts were written** (nubia-kush.md mtime 17:20:04 < receipt mtimes 17:20:41 / 17:23:55).
  No content lines changed, so the evidence stands; the hash/line metadata does not.
- Recommendation to the integrator: treat receipt hashes/locators as timestamped snapshots, or have the sweep
  run before the F shards. Do not let the round-8 harness compare `entry_sha256` for equality against live files.

**3.2 Raw-label preservation is satisfied, via `reconciliation.json`, not via every receipt.**
`reconciliation.json` (sha256 `204ec38a…` at 17:26:41) preserves all 15 raw round-6 labels and scopes; I re-derived
the 15 `(verdict, support_scope)` pairs from `corpus/lessons/round-6-sources/*.json` and compared: **15/15 MATCH,
0 mismatches**. Two receipts do not carry the raw label themselves (F01: none; F05: `worker_disposition` only);
the claim's wording places raw labels in `reconciliation.json`, so the requirement is met — but the two receipts
would be self-inconsistent if read alone. Note: `reconciliation.json` was generated by the F15 shard, which also
re-adjudicated its own row (`round8_recheck.adjudicated_by: "FRESHNESS R8-F15 shard"`, disclosed in-file);
no sibling row was re-adjudicated. Independence caveat, not a defect.
Transient observation: at 17:24:5x the file was briefly mid-write and failed `json.load` ("Illegal trailing comma…");
valid from 17:25:35, and its recorded F15 receipt hash (`295509aa…`) matches the file.

**3.3 F02's proposed disposition is not the one carried in `reconciliation.json`.**
`reconciliation.json` (generated 17:24:00Z) carries F02's round-6 reconciled disposition `unresolved`, while the
F02 receipt (landed 17:28) proposes `reconciled_disposition.disposition: "resolved"` for the object/scholarly legs.
Both are labelled: the reconciliation file says it carries round-6 dispositions for F01–F14 and did not re-adjudicate
siblings; the receipt says the round-6 "unresolved" was grounded in unretrieved object and scholarly legs, now retrieved.
The parent must pick one for the F claim's after-state; I do not adjudicate it here.

**3.4 Schema heterogeneity vs the round-8 acceptance harness.**
Receipt field names vary (F01 `quoted_passage`; F02 `fresh_retrievals`; F04/F05 `passages`; F07/F12 `fresh_retrievals`;
F08 `additional_retrievals`; F10 `retrieved_passages`; F15 `retrievals`; support under `support_scope`,
`passage_support`, `passage_support_scope`, `passage_vs_whole_claim`). The current `reports/round-8/validation.json`
records F failures such as "passage support and whole-claim support are not held in separate fields" for F01/F06/F14 —
receipts that do carry equivalent fields under other names. The harness run also predates 8 of the 15 receipts.
Recommend a synonym set in the harness before the final count; the raw receipts themselves are compliant.

**3.5 Minor accuracy notes.**
F12's `scope_notes` attributes `reconciliation.json` to "X02 shard"; it was written by the F15 shard (per its
`generated_by` field). F07's main-leg content is a re-confirmation of the same verbatim passages as round 6 —
the claim requires a fresh retrieval record, which it is; new content value rests on its independent additions
(UNESCO WHC, SCIO, Britannica, Wikipedia). Neither affects a verdict.

## 4. Negative-claim sweep coverage

Every receipt that makes a negative or absence claim carries its sweep/commands: F01, F02, F03, F04, F05, F06
(`evidence_commands`), F08, F09, F10, F11, F12 (`evidence_commands`), F13. F14/F15 make no negative claim
(F14's `counts` include `excerpts_over_40_words: 0` as a self-count, not a negative source claim).

## 5. What this audit does and does not establish

- Establishes: the quoted passages exist at the locations claimed, on 2026-10-17, for all 15 receipts;
  claimed artifact hashes are reproducible; accessed-at values are consistent with file mtimes (no future-dated
  or off-date timestamps: checked all ISO timestamps in all receipts against mtimes).
- Does not establish: truth of the underlying scholarship, whole-claim resolution, or that any entry edit is
  warranted. Verdicts here are about receipt quality, per the X02 assignment.

## 6. Notes for the integrator

1. F claim after-state ("≥8 of the 15 show a retrieved substantive passage") is comfortably met on my count:
   all 15 carry at least one substantive retrieved passage; the harness's own field-name-strict check undercounts
   (see §3.4) and its recorded run predates most receipts.
2. Entry hashes in receipts are snapshots; the sweep finished after most shards measured (§3.1).
3. F02's disposition needs the parent's call (§3.3).
4. The only re-verification I could not complete is F02-P2 (Perseus LSJ, HTTP 503 to me on 2026-10-17); that leg
   stays `to-verify` from this auditor's chair, not because the receipt is suspect.

## 7. Receipt state at audit close (2026-10-17T17:29:40-03:00)

`sha256sum reports/round-8/freshness/R8-F*-receipt.json reports/round-8/freshness/reconciliation.json` at that time:

```
R8-F01 5965991ea94cd22423af6ec1a05d6a75c1a28ae19dad95295c58602db7484ddb
R8-F02 81c37d9ad8c4aa2efd6f7d144d110c33e21a813ad0dcbff33c189764957a1323
R8-F03 2024e4a7261a63fcc11021d001560156d943964539ec329b8ab5949cec638711
R8-F04 7643248482b87393f605b82d3c15826b20e6290c9ea1746f32e31271f7990bcb
R8-F05 e75b682591c627a6a1953f9a9ab360bd577cc33e95a18b57e8ecf909fb34dc88
R8-F06 1234f42df338070efc2267e7b076acb88af5357ced4ea905b7ebebd7e6f6962d
R8-F07 2398cf8aff03a2c06abc1e5a8014b787d501c067846c29c13e127db435cb52cf
R8-F08 ca26c8e53a25757c0505db69c3a2a386bbc5320f28ffd2a5322df5ec218d43d0
R8-F09 d15898fa2504c8deffc2666ec03c23909e6cf0a6fae96c97039989a82d139c1e
R8-F10 ccbfa18f520f27a24ff1888e80e800d83b6029c32cb1f03bc633cffeb8d26ab4
R8-F11 a94509e5ecc51b680b4d4913dfc81c302688074972176e32dda6ec90ac40d33c
R8-F12 5ce0eb137c86e3e5a221e5cf859820bb873d132fe811ac619db2d260f37a4d8a
R8-F13 87514dad719ddbcde739da73fbd0d50ad669d274458c4502cd2ff4f1555ac4d5
R8-F14 f269ff9d00bbd698c3c3497dcd0985827938bbd56080d0bfda594a9fb25a1cec
R8-F15 295509aa305f7ba488c251375d089f1aa0e6c793b2011b7c10498cff317ad870
reconciliation.json 204ec38aa413b185c1dba6da4a587291d665701ad4735cb3b0641d65fbed43d3
```

Two receipts were updated after my first read and are now live-consistent: F02 (landed 17:28, entry hash = live)
and F03 (rewritten 17:27:55; it now carries `entry_post_filing_change` documenting the same metadata-sweep drift
as §3.1, with `sha256_after a8e421f7…` = live). Verdicts in §1 stand on re-read of both final versions.
Any receipt changed after 17:29:40 is outside this audit.
