# RevRowS696 — claim C row S696 blind support review

Seat: kotodama-r63-w1-RevRowS696 (reviewer, leaf). Date: 2026-10-23.
Item: BLIND SUPPORT, claim C, row S696 (Roman military crowns: corona civica /
corona muralis / corona obsidionalis). My report path: .ufo/waves/round-63/w1/RevRowS696.md.

## 1. What was available
- ScribeRowS696 scratch was EMPTY at my start (checked repeatedly). I performed
  the assignment's independent fallback: found my own page for the same subtopic
  and verified it by ordinary means, before receiving any scribe draft.
- The scribe later published /fast/scratch/hyaku/kotodama-r63/ScribeRowS696/
  review-draft.txt (draft quote, bullet, incomplete row with UNRESOLVED capture).
  I reviewed that draft against my independent verification.

## 2. Independent page (same subtopic)
- LacusCurtius, Smith's Dictionary of Greek and Roman Antiquities (John Murray,
  1875), "Corona" entry, fetched by ordinary plain GET:
  http://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html
  → HTTP 200, 65,691 bytes, text/html. (Same source the scribe independently
  chose; my fetch preceded and did not rely on their draft.)

## 3. Quote verification, LIVE URL (locator: reports/round-61/reopen-quote.py)
Draft quote (11 normalised words): “Among the honorary crowns bestowed by the
Romans for military achievements”
- Locator: `LOCATED http://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Corona.html` (exit 0).
- Body-text confirmation (HTMLParser over saved page): the span sits inside a
  `<P CLASS="justify" ID="obsidionalis">` body paragraph, not a caption/alt/
  title/meta attribute. Pasted located span (verbatim): "I. Corona Obsidionalis.
  Among the honorary crowns bestowed by the Romans for military achievements, the
  most difficult of attainment, and the one which conferred the highest honour,
  was the corona obsidionalis, presented by a beleaguered army …" — quote = the
  11-word clause at its start.
- Additional independent span I verified on the same page (20 normalised words):
  "The first man who scaled the wall of a besieged city was presented by his
  commander with a mural crown" → LOCATED (exit 0), body `<P ID="muralis">`.

## 4. Entry bullet fidelity (draft bullet)
Draft bullet: "Crowns bestowed by the Romans for military achievements carried
distinct forms and assigned purposes. (S696)"
- Shared-with-quote content words (in quote order): crowns, bestowed, Romans,
  military, achievements (≥ 3 required; satisfied). Longest copied run =
  "bestowed by the Romans for military achievements" (7 words ≤ 12).
- No invented dates or peoples. "Distinct forms and assigned purposes" is
  carried by the same page's body (section II civica = citizen-rescue crown;
  IV muralis = wall-assault crown; I obsidionalis = siege-relief crown; all
  verified verbatim in body paragraphs). No claim in the bullet goes beyond the
  page.

## 5. Capture verification — BLOCKED at this seat
All ordinary-means attempts to reach the Wayback capture failed within my budget:
- CDX `https://web.archive.org/cdx/search/cdx?url=<page>&output=json&limit=-5&filter=statuscode:200`: first request returned data (7 lines = 5 rows), then persistent HTTP 429, later HTTP 403 (identical for encoded/raw URL forms).
- Wayback availability API: HTTP 429.
- Memento timemap: ECONNREFUSED. timetravel.mementoweb.org: DNS ENOTFOUND.
- Direct replay probe `…/web/<ts>id_/<page>`: HTTP 403.
- Bash egress to web.archive.org/archive.org: connection refused (no route); live penelope.uchicago.edu worked.
Consequences: no verified timestamp/capture for the page; the scribe's row is
also incomplete (capture UNRESOLVED, marked do-not-land). The drafted ROW is
therefore not yet in verifiable final form.

## 6. Verdict
- SUPPORTED — for every element that exists to check: the drafted quote is
  verbatim body text on the live URL (8–25 normalised words), the entry bullet
  restates only what the quote/page carries (no invented claims), and the page
  is on-subtopic (Roman military crowns, valour-award crowns).
- NOT-YET-VERIFIABLE — the capture half of the row: blocked by persistent
  Wayback 429/403 at this seat and at the scribe's (shared rate-limit/egress;
  recorded as met-not-passed for no challenge was routed, the services just
  refused). Re-run the capture lookup (CDX → id_ replay) when the rate-limit
  clears, then re-verify the same quote on the capture and confirm the row's
  capture URL embeds the same original URL.
- No fabrication: the located spans above are pasted from fetched bytes; the
  capture status is exactly as observed.

## 7. Residual risk / verification gaps
1. Capture same-page + same-quote confirmation: OPEN (blocked as above).
2. Final registry row text (11 columns) not landed yet — re-check quote/entry
   fidelity against the final committed row wording.
3. My live check used the http:// variant; the scribe's row lists the https://
   variant — locator LOCATED on both (their message confirms https LOCATED).
4. The `*` in the URL path is real (the site serves it); Wayback matching may
   vary by encoding — use exact match on capture discovery.
