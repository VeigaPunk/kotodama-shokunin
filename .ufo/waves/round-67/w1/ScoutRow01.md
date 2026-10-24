# ScoutRow01 — r67 rows S805, S806 (claim C, medicine/healing register)

Both rows opened, verified live with curl, captured in Wayback, and written to
`.ufo/waves/round-67/rows/ScoutRow01/row-S805.txt` / `row-S806.txt`.

## S805 — Hippocratic corpus / humoral canon (tier B)
- Source: Michael Boylan, "Hippocrates (c. 450-c. 380 B.C.E.)", Internet
  Encyclopedia of Philosophy (IEP, U. Tennessee at Martin; peer-reviewed
  entries). `https://iep.utm.edu/hippocra/` — HTTP 200, 50,078 bytes,
  no redirect, no login. Anchor quote verified verbatim in §"The Four Humors":
  "the doctrine of the four humors of the body: blood, phlegm, black bile,
  and yellow bile".
- Capture: `20260929171735id_` (200; body gzipped — `curl --compressed` or
  `zcat` needed to grep; anchor confirmed inside).
- Rejected alternates (in-flight, not written to rejects.txt since not
  formally proposed): Perseus `hopper/text?doc=Perseus:text:1999.01.0249`
  resolves to *Ancient Medicine*, not *On the Nature of Man*; the
  canonical-greekLit repo has a stub textgroup `tlg0627` with no works;
  scaife.perseus.org serves a JS shell (7.4KB, quote not in curl body);
  MIT classics.mit.edu has no `naturman` page (index lists 17 treatises,
  none On the Nature of Man); NLM hmd/topics/greek-medicine page was a
  viable fallback (usable humors sentence) but IEP names the Coan doctrine
  more precisely.

## S806 — Ayurveda / Charaka Samhita / doshas (tier A)
- Source: Jaiswal & Williams, "A glimpse of Ayurveda — The forgotten history
  and principles of Indian traditional medicine", J Tradit Complement Med
  7(1):50-53 (2017), PMC full text.
  `https://pmc.ncbi.nlm.nih.gov/articles/PMC5198827/` — HTTP 200, 142,690
  bytes, no redirect. Anchor quote verified verbatim in §3: "Vata dosha ,
  Pitta dosha and Kapha dosha are collectively called as Tridoshas"
  (page renders with space-padded punctuation and curly quotes).
- Capture: `20260614165133id_` (200; "Tridoshas" + anchor confirmed).

## Checks performed
- Uniqueness: both live URLs grep 0 hits in `corpus/SOURCES.md`; the only
  IEP rows anywhere are `iep.utm.edu/fallacy/` and `iep.utm.edu/xunzi/`
  (different paths → distinct normalized URLs). No PMC5198827 anywhere.
- Cell geometry (self-check vs accept-c.py rules): 11 cells each; kind
  `docs`/`paper`; tier B/A; scope 51/49 chars; quotes 16/13 words; teaches
  cells 189/190 chars; bullets 18/17 words, ≥3 in-order quote content words
  (4 / 7), teaches coverage 0.077 / ~0, novel words present.
- Hosts: `iep.utm.edu` and `pmc.ncbi.nlm.nih.gov` — two distinct hosts
  toward the ≥10-host leg.

## Remaining unknowns / handoff notes
- Wayback capture for IEP returns `Content-Encoding: gzip` even without
  `Accept-Encoding` — re-openers should use `curl --compressed`.
- The PMC page uses curly quotes and odd spacing (" , " before punctuation);
  the anchor quote is copied verbatim from the normalized body text —
  extraction renders `“ Tridoshas ”` with internal spaces; the anchor I
  stored drops the curly marks (straight quotes wrap it per row format).
- No rejects file needed: no candidate was committed then rejected.

## Tooling
No installs or upgrades performed; stock curl/python3 sufficed.

## Design finding (resolved by L1)
Cross-seat conflict noted in-flight: accept-c.py APPEND bounds new ids to
S805-S828 ∪ {S801-S804}, while accept-ca.py D4 needs >=6 rejects opened
2026-10-24 (S801-S804 + 2 new ids). L1 resolved via per-claim lands
separation — claim C's receipt runs at its own lands commit A_c where only
S805-S828 append; Ca's later lands commit carries the S829+ rejects. No
counter/claims revision; S805/S806 are unaffected either way.
