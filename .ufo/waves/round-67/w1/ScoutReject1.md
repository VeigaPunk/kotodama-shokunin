# ScoutReject1 — reject-candidate item (claim C gate), round 67

## Deliverables written
- `.ufo/waves/round-67/rows/ScoutReject1/row-S829.txt` — rejected row, **paywall/JS-wall class**
- `.ufo/waves/round-67/rows/ScoutReject1/row-S830.txt` — rejected row, **duplicate-of-rowed-URL class**
- `.ufo/waves/round-67/rows/ScoutReject1/rejects.txt` — 5 surveyed-but-not-rowed candidates with evidence

Both rows keep the ROW= eleven-cell shape (id|source|kind|tier|scope|anchor|teaches|status|opened|recheck|used-by)
with `status=rejected`, teaches `REJECTED: <reason>; flip: <change>` (<240 chars), opened 2026-10-24,
used-by `—`, and full VERIFY/CAPTURE/ACCESS blocks matching the r66 fragment format (ScoutReject01/row-S801.txt).

## S829 — Anne Hudson Jones, "Literature and medicine: physician-poets," The Lancet 349(9047):275-278 (1997)
- Observed: `curl -s` on the live URL → **HTTP 403, 5,632 B, 0 redirects, `<title>Just a moment...`**
  (Cloudflare interstitial), identical on retry. Article identity verified via Crossref
  (`api.crossref.org/works/10.1016/S0140-6736(96)12240-6`). `archive.org/wayback/available` →
  `archived_snapshots {}` — no capture exists.
- Reject class: paywalled/JS-walled source a plain curl cannot open (QUALITY criterion 10: nothing
  quotable was opened; domain wall, not an article-specific block).
- Confidence: high. The 403+challenge is byte-verified twice; DOI→article mapping is Crossref-verified.
- [INFERENCE] A headless-browser seat could pass the challenge, which is exactly why the flip condition names an "openly reachable copy," not browser bypass.
## Design finding: C-APPEND vs Ca-D4 id conflict (resolved by L1)
- Conflict (CriticFrontier alert): accept-c.py APPEND bounds new registry ids to
  S805-S828 ∪ {S801-S804}; accept-ca.py D4 requires >=6 status=rejected rows opened
  2026-10-24 (S801-S804 + >=2 new). Any new reject id (these S829/S830) lands inside
  the C lands window => APPEND FAIL extra=[S829,S830]; jointly unsatisfiable at a
  single lands commit.
- L1 ruling (received mid-survey, in force): **no counter/claims revision**. Per-claim
  lands separation — C's receipt is evaluated at its own lands commit A_c where only
  S805-S828 append over base (A_r carrying S801-S804 lands before A_c); Ca's lands
  commit A_ca comes later and carries the S829+ reject rows plus the round-67 lesson.
  Consequence for the L1 integrator: **rows/ScoutReject1/row-S829.txt and
  row-S830.txt must be appended to corpus/SOURCES.md in the A_ca commit, NOT before
  A_c** — sequencing, not content, is the correctness condition.

## S830 — Science Museum Group object co122693, "Disease mask for healing rituals" (A19437)
- Observed: the candidate's live URL is **already rowed** — `corpus/SOURCES.md:281` row **S252**
  carries `https://collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals`
  (tier A, mined 2026-10-22, Sri Lankan sanni healing-ritual mask — squarely medicine/healing).
- Reject class: duplicate of an existing row's live URL; second row would add zero new sourcing.
- Confidence: high — the dup is a literal string equality inside the registry.
- Note: live re-fetch returned **HTTP 429** (SMG rate-limits this host; S252's own provenance records a
  429-then-200 session). Duplicate verdict rests on registry-side URL equality + wayback capture
  20260417222314 (HTTP 200), stated explicitly in the row's VERIFY/ACCESS.

## rejects.txt highlights (surveyed, not rowed)
- ScienceDirect PII S0378874110006474: 403 + 832 KB challenge shell — weaker wall datum than S829.
- JSTOR stable 24620628: HTTP 200 but body is a 3,038 B "Client Challenge" page — same class as S829.
- SMG co107623 animal-tail medicine-man amulet: 429-limited (transient, not hard reject).
- Commons "Doctor Schnabel von Rom" file page: HTTP 200, only quotable text is the caption —
  rejectable caption-only class, held back as borderline (engraved poem is primary text).
- sacred-texts.com healing incantations: lore-canon sibling-lane scope; class surveyed, no URL rowed.

## Caveats / remaining unknowns
- SMG host rate-limited all probes after first hit (429); S830's reject needs no live bytes (registry
  equality suffices), but any future SMG candidate should budget a retry window.
- S829 has no wayback capture at all — the flip cannot be satisfied by capture alone.
- Tools: no installs needed (curl, python3 stdlib, system grep only).

Report: .ufo/waves/round-67/w1/ScoutReject1.md
