# ScoutReject2 — r67 reject-candidate findings

Two first-class rejected registry rows written, classes disjoint from ScoutReject1 (who took Cloudflare-403 paywall [S829 Lancet] and duplicate-URL [S830 SMG]):

## S831 — bot-challenge (JS client-challenge) REJECT
`rows/ScoutReject2/row-S831.txt`
Edelstein 1937, "Greek Medicine in Its Relation to Religion and Magic", Bull. Inst. Hist. Med. 5(3):201–246 — squarely inside the medicine/healing register and a genuinely useful source (cited ~200×).
- VERIFY: `https://www.jstor.org/stable/44438180` → HTTP 200 but only 3,038 bytes: `<title>Client Challenge</title>`, assets under `/_fs-ch-*`, "JavaScript is disabled in your browser". Zero article bytes. Stealth wall: 200 status + plausible byte size means it passes naive curl checks and must be caught by reading.
- Precedent: S132 (Battison re-open → 403 Cloudflare → REJECTED, unopened per QUALITY criterion 10).
- CAPTURE: Wayback snapshot 20240310013528 exists (of JSTOR's shell).
- Flip: ordinary-means copy (publisher PDF, library scan, open deposit — the article is 1937 and exists in reprint collections).

## S832 — metadata-only landing page REJECT
`rows/ScoutReject2/row-S832.txt`
Wellcome 1988 exhibition catalogue "Hygieia's handmaids: women, health, and healing" (Hall ed.), IA item b20456943 — medicine-register relevant (women healers, domestic medicine).
- VERIFY: `https://archive.org/details/b20456943` → HTTP 200, 241KB — but the body is record metadata + BookReader viewer chrome (IN COLLECTIONS, SHOW ALL); no catalogue prose. The quotable text lives in `/download/b20456943/b20456943_djvu.txt` and `.pdf` (metadata API: 31 files).
- Precedent: registry cites stream/leaf URLs (S298 djvu.txt, S306 page image, S371 djvu.txt), never bare details pages — so the details URL is a reject as a *support URL*: it resolves to no quotable text for a checker.
- CAPTURE: no Wayback snapshot (explicit no-capture reason recorded).
- Flip: cite the text-stream or leaf-image URL directly — the item itself is public-domain Wellcome digitisation and fully rowable once the stream URL fronts it.

## Registry shape compliance
Both rows: 11 cells; kind in enum (paper/book); tier A/B honest for the underlying work; status `rejected`; teaches = `REJECTED: <reason>; flip: <verdict-changer>` (217/225 chars ≤240); opened 2026-10-24; recheck 365d (matches existing rejected rows S028-S047, S132); used-by `—`; anchor cell describes what is actually reachable at the URL. Feeds accept-ca.py D4 (`rejected` + opened 2026-10-24 → ≥2 new rejected rows) and the ScribeGateRows rejected-Gate lines.

## Surveyed not rowed
`rows/ScoutReject2/rejects.txt`: 11 further candidates with live probe results (OUP SHM 403, HathiTrust 403, T&F/Wiley/ScienceDirect/BMJ/LoC challenges, Wikipedia History-of-medicine tier-C, Wellcome works 405, NLM Primo timeout). Noted overlaps with ScoutReject1's classes flagged.

## Confidence & gaps
- HIGH: both reject verdicts and their evidence (curl outputs observed directly).
- MEDIUM: S832 class assignment — a sibling could argue the details page is "opened" because metadata is quotable; I recorded the strict reading (support URL must resolve to the cited text) plus the flip that makes the source usable.
- Disjointness: verified against ScoutReject1's landed S829/S830 files — no URL, host, or class collision.
- Conflict note (CriticFrontier alert, verified from source): accept-c.py APPEND bounds new ids to S805-S828∪{S801-S804} (l.357-358) while accept-ca.py D4 requires >=6 rejected rows opened 2026-10-24 (l.235), i.e. S829-S832 must append. L1 resolution (no counter revision): per-claim lands separation — C's receipt runs at commit A_c where only S805-S828 append; Ca's receipt runs at later commit A_ca which carries S829-S832 + the round-67 lesson. These two row files therefore land at A_ca, not at C's lands commit — placement dependency for the integrator, not a defect in the rows.

Report: .ufo/waves/round-67/w1/ScoutReject2.md
