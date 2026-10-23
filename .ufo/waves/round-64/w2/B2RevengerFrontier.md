# B2RevengerFrontier — round-63 reconstruction vs records

Deliverable: `/home/vgpnk/.cache/hyaku/kotodama-r64/w2/B2RevengerFrontier/revenger.md` (full reconstruction, evidence chains, confidence marks). Read-only audit at base `ff30a20`; no lane files touched except this report.

## 6-line summary

1. Round 63 landed `8d2041fa`: entry + 24 rows appended (619→643), README row + counts; all 24 Gate quotes appear inside their row's anchor cell — none missing — but 6 are truncated prefixes (S697/S701/S705/S715/S717) and S703 diverges by one apostrophe byte (Gate `'`, anchor `’`).
2. The r63 entry dropped the r61 exemplar's provenance trio (`source:`/`verified-at:`/`recheck:`) — routed defect 6; a round-64 entry must restore it.
3. `row-verify.txt` LOCATED only 19/24 rows: S702, S706, S715, S716, S717 never located there (S706/S716 refused as "quote under 8 words"); the LIVE leg later passed S702/S706; S715/S716/S717 landed on scribe-reported live LOCATED only — the lesson's "every quote re-verified at integration" is false as written.
4. Only S694, S702, S709 have a recorded LOCATED on their capture URL; S711/S713/S715 captures have no recorded fetch at all — ROWS leg checks capture shape only, so "capture verified" is not an inheritable claim.
5. Integration silently re-sourced S696 (LacusCurtius→coronet), S710 (Britannica→tiara), S714 (IWM→shako), S703 (scribe filed no row); RevRowS694 raced to NOT-SUPPORTED-on-absence and RevRowS696/S705 reviewed different pages than landed.
6. Uninheritable records: tier histogram "A 14/B 10" (actual 13/11); dead pointer `final-measures.txt` in SCORECARD/corpus/LOG.md; "45 seat reports" (47 actual); S696-coronet "verified live in §4" with no §4 evidence; LOG written to `corpus/LOG.md` not root `LOG.md`; S687 mined-but-unused (r64 must flip to `queued`).

## What a round-64 row must copy / not copy (compressed)

Copy: row cell discipline, capture `id_` shape with embedded original == live, verbatim locator receipts including failures, one-S-id bullets, README topic-verbatim row, append-only registry. Not copy: missing provenance trio, rows landed with no recorded live LOCATED or no capture fetch, unrecorded integration re-sourcing, Gate quotes that are truncated or typographically divergent from the anchor span, prose-only rejects (r64 pins six disposition rows S744-S749), approximate counts/dead pointers, `corpus/LOG.md`, receipts without a measured-revision line.

## Tooling

None installed; audit used git read-only + grep + python3 byte comparison only.

Report: `.ufo/waves/round-64/w2/B2RevengerFrontier.md`
