# ReviewerC94 — wave report (round 94)

Seat: read-only attacker on claims C (coverage) and A (adjacency). Full findings: stage/ReviewerC94/review.md (11,927 bytes, numbered A1–A4, C1–C9).

## Findings count by severity
- Blocking: 1 (A1 — claim A fails its own frozen kill_rule)
- Routed: 3 (A2 verified-but-declined remedy; C1 counter-semantics hazard; C2 missing search-log note in staged registry lands)
- Notes: 9 (A3, A4, C3–C9)

## Verdicts
- Claim C: HOLDS — all six ENTRY checks, SOURCES (5 rows S965–S969, tier A, mined, opened 2026-11-05, quoted, all cited), APPENDONLY (0 removed / 6 added lines vs base), INDEX (findings=0), CENSUS (rc 0) measured green on an assembled lands tree. Two integration flags for the L1 (C1, C2).
- Claim A: DEFECT-LIST — the patch is semantically correct and scope-clean (only the two named lines change; the owner pointer changed, not deleted; cross-domain claims preserved), but the frozen predispatch counter reports `A1 dangling-greeting-pointers 2` after it because its `"greet" not in t` filter excludes the owner target from resolution. L1 must amend the counter at integration or accept A as failed. A verified A1=0 remedy exists (two non-"greet"-named, greet-mentioning co-targets) but the executor declined it as a decoy; recorded.

## Quote-check counts
- Registry-row quotes: 19/19 PASS as exact substrings of the committed captures (raw for pdftotext .txt captures, raw + rendered for .html captures; word counts 8–22, all ≤ 25; each primary quote exactly one occurrence).
- Entry quotes: 15 quoted spans; 14 locate uniquely in the capture of the S-id cited on the same line; 1 is the NON-CANON invented song name (correctly not a capture quote).
- Capture integrity: 8/8 sha256 recomputed and matched; live re-fetch HEAD 200 ×5 and full-GET sha256 equality ×5.

## Other checks (commands in review.md)
- S-id discipline: DEFECTS 0 (script output pasted in review.md source run).
- Fact support: 13/13 sourced sentences supported; 2 framing notes (Connemara "single exception" omits a second captured exception; L182 rhythm/meaning direction reversed vs capture).
- Design labelling: NON-CANON present ×3; 0 canon claims; table rows labelled 26/26; 2 benign unlabelled non-label-scope lines.
- Duplication: none — entry follows the connector's narrowing prescription (boundaries named, owners coupled, IDS/epic/liturgy/music excluded).

## Tooling installed
None. pacman: not invoked. Sysctls: untouched. Scratch /fast/scratch/hyaku/kotodama-r94/ReviewerC94/ deleted before yield.

## Blockers
None for this seat. The claim-A counter-vs-claim inconsistency (A1) is a decision that belongs to the L1 at integration, not to this seat.
