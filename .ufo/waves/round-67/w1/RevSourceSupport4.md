# RevSourceSupport4 — blind-support review, rows S823–S828

Seat: reviewer (blind support), round 67 wave `kotodama-r67-v2`.
Contract inherited from RevSourceSupport1: for each row, open the fragment, re-fetch the live URL myself,
capture it, verify the anchor quote in body text, then judge whether the `teaches` cell is actually
supported (not merely quotable). One verdict per id with evidence.

**LSP:** no `lsp` device is exposed in this seat's toolset, so definition/reference/diagnostics checks
were unavailable; all file inspection below is literal `grep`/`read` and is labelled as such, never as
semantic proof.

## Dependency (blocking for the fragment half of the contract)

At review time the wave's row fragments do not exist on disk:

```
$ find .ufo/waves/round-67 -maxdepth 2 -type d
.ufo/waves/round-67
.ufo/waves/round-67/stage
.ufo/waves/round-67/stage/mut-o     <- only mutant sources
.ufo/waves/round-67/w1
$ grep -rn "ROW=S82" .ufo/waves/round-67   # no hits
$ grep -cE '^\| S8[0-9]{2} ' corpus/SOURCES.md  -> S800 only (852); S805-S828 absent
```

So this is a **pre-fragment blind review**: it fixes the source-support envelope each of S823–S828 must
land inside, and names the drafts that will fail the counter or the lesson gate if they go the obvious way.
When the fragments land, the only untouched part of my contract is quote-in-body re-verification per
fragment, which the L1 must re-run against the exact fragment anchors.

## Per-row verdicts

### S823 — "Medieval European surgical guilds and barber-surgeons" — SUPPORTED (narrowed)
Verified live (HTTP 200, 69,448 bytes):
`https://www.rcseng.ac.uk/about-the-rcs/history-of-the-rcs/`
Body text, verbatim: *"The Company of Barber-Surgeons, established in 1540, was a trade guild and a
London Livery Company that apprenticed and examined trainees within the City of London."* … *"In 1745,
the Barber-Surgeons were split by an Act of Parliament into two bodies at the request of the surgeons."*
Wayback capture exists: `web.archive.org/web/20260903174248/https://www.rcseng.ac.uk/...`.

- Supported teaches: guild status, 1540 union, apprenticeship + examination as the training route,
  1745 split. That is the whole of the *guild* claim.
- **Defect risk (MEDIUM):** the natural anchor is 26 words, over the ≤25-word `## Gate` limit in the
  lesson. A verbatim 17-word sub-span exists inside the same sentence: *"established in 1540, was a trade
  guild and a London Livery Company that apprenticed and examined trainees"* — use that, do not paraphrase.
- **Defect risk (MEDIUM):** "medieval" is not this source's word; RCS dates the *Company* to 1540 (early
  modern). If `teaches` says "medieval barber-surgeons", the claim needs a different body sentence. The
  Science Museum Group people record `cp47957` does carry the medieval framing ("one of the most common
  medical practitioners of medieval Europe … charged with looking after soldiers") and *does* have a
  wayback snapshot (`archive.org/wayback/available` → available), but the live page answered HTTP **429**
  on every direct attempt, so its body text could not be verified from this seat — it can only carry the
  anchor after a paced fetch confirms the quoted sentence.
- Tier: B, honestly. It is an institutional self-history page with no named author; A would be
  over-claiming for a scope broader than RCS's own institutional record.

### S824 — "African healing systems and the sangoma/nganga" — PARTLY SUPPORTED, scope defect (HIGH)
Verified live (HTTP 200, 1,189,959 bytes), Phansi Museum story on Google Arts & Culture:
`https://artsandculture.google.com/story/medicine-mending-and-mastery-southern-africa-39-s-traditional-healers-phansi-museum/9QURcl79b3cD3A`
Body text, verbatim: *"Sangomas are shamanic practitioners or spirit mediums who work within many southern
African cultures. Highly skilled individuals, they are able to communicate with the ancestors to help cure
afflictions and work with indigenous plants …"*

- The **sangoma** half is supported by a museum-published interpretive text.
- **HIGH — conflation:** the topic pairs *sangoma* (Nguni/Sotho/Tsonga southern Africa) with *nganga*
  (Kongo, and the Tsonga cognate *n'anga*). No single body I could verify states them as one system; the
  lane's own registry already carries *nganga* only as a Kongo ritual-specialist credit (S395, S400, S402:
  "artist credited as … nganga"). A `teaches` cell asserting a shared "African healing system" would be
  supported by neither source. Either narrow `teaches` to the verified sentence (spirit medium, ancestor
  communication, plant medicine) or split the row's scope to southern Africa and drop *nganga*.
- **HIGH — capture blocker:** this story page has **no wayback snapshot** (availability query returned
  `"archived_snapshots": {}`). Under ACCEPT-C-67 `CAPTURE` that forces the `no-capture` reason token, which
  has **zero precedent in the registry** (grep count = 0 across 724 rows). Prefer a host that archives:
  the Adler Museum page `https://www.wits.ac.za/health/adlermuseum/` is live (HTTP 200) but its only
  sangoma text is *"A patient consulting a sangoma (traditional healer)"* — a reconstruction caption, too
  thin to support a `teaches` cell (tier B at best, one fact).
- Tier: B (museum interpretive text), not A.

### S825 — "Greek healing sanctuaries (asklepieia) and incubation" — SUPPORTED by UCL/Warwick, NOT by UNESCO
Verified live (HTTP 200, 11,908 bytes), UCL *Dreams in Ancient Medicine*:
`https://www.homepages.ucl.ac.uk/~ucgajpd/medicina%20antiqua/sa_dreams.html`
Body text, verbatim: *"the vast majority of cures recorded on the stelae come after the ailing suppliants
have slept in the sanctuary in hopes of a cure. This practice is called "incubation.""*
Verified live (HTTP 200, 45,751 bytes), Warwick *Sanctuary of Asklepios, Epidaurus*:
`https://warwick.ac.uk/fac/arts/classics/intranets/students/modules/greekreligion/database/clumcc/`
Body text: *"they would make sacrifices to Asclepios and purify themsleves before entering the abaton …
Aside from incubation, pilgrims could also be given pharmaceutical drugs and remedies, they could even
undergo surgical treatment, evident due to the scalpels, lances and other instruments found there."*

- **MEDIUM — wrong source for the topic's second leg:** the UNESCO Epidaurus page
  (`https://whc.unesco.org/en/list/491/`, live, captured at `20261011220730`) was fetched and its full body
  contains **no occurrence of "incubat"**; it only says the site has *"temples and hospital buildings
  devoted to its healing gods"*. A fragment using UNESCO for an incubation `teaches` would be a false
  anchor. UNESCO is fine for a sanctuary-as-institution claim only.
- **MEDIUM — register overlap:** incubation/Asklepieia is already owned in-corpus, by name:
  `corpus/knowledge/myth-symbol/divination-omen-systems.md:89,126,135,186` (dream-oracle & incubation row,
  *iamata* case archive) and `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md:37,52,77,114,173`
  (healing/incubation shrine, iamata). The medicine entry must point one-way at both and must not re-own
  divination. The row's `teaches` should be *sanctuary medicine as practice* (drugs, surgery, incubation
  as therapy delivered at a sanctuary), not "incubation is a Greek divination technique".
- Tier: B for both (UCL is a teaching resource; Warwick is a departmental database page). A would need the
  *iamata* edition (IG IV²,1) or an original paper. Capture status: Warwick has a wayback snapshot, **UCL
  has none** — so the anchor must sit on the Warwick text, or the row needs the `no-capture` token.

### S826 — "Japanese moxibustion and acupuncture transmission" — SUPPORTED (abstract-anchored)
Verified live (HTTP 200, 104,587 bytes), J-STAGE, *Japanese acupuncture and moxibustion in 16–18th-century
Europe*, J. Japan Acupuncture & Moxibustion Society 61(2):
`https://www.jstage.jst.go.jp/article/jjsam/61/2/61_2_150/_article/-char/en`
Abstract body, verbatim: *"…by Hermann Buschoff, a Dutch clergyman in Batavia, about a remedy against
Podagra that he called Moxa (in Japanese, mogusa)."* (also Cleyer, Dejima, ten Rhijne in the same abstract)

- Supported teaches: moxa as *mogusa*, the Buschoff→Cleyer naming/manufacture episode, the Dutch-post
  channel of transmission. That is exactly the assigned topic (transmission), so this is the strongest of
  the six.
- **MEDIUM:** only the abstract is public on the page (5,731 chars of text); the anchor must be a verbatim
  abstract span, and `teaches` must not borrow facts from the full text the page does not display. Also
  *no wayback snapshot* exists for this URL — capture is the blocker again. Museum objects that would
  supply material evidence (SMG `co8010533` moxa plugs, `co8010489` moxa caps, the 1681 acupuncture model)
  are HTTP **429** to direct fetch and unarchived, so they cannot be the anchor either.
- Tier: A for the abstract sentence (original peer-reviewed paper); B if the row leans on the museum
  objects.

### S827 — "The medieval plague treatises / consilia" — UNVERIFIED CANDIDATE (evidence gap declared)
I did **not** fetch a body text for this row, so no support verdict is possible from this seat. The best
open lead is Di Segni's article on Gentile da Foligno's *Consilium contra pestilentiam*:
`https://air.unimi.it/retrieve/ef437c27-e994-4c01-9225-c1fbe0d4c1aa/Gentile+da+Foligno+OA.pdf`
(seen only as a search-result abstract: numerous *consilia* for specific diseases, the 1348 Pisa
*consilium*, Hebrew translation, air-purification/vinegar/diet advice, theriac with cheaper substitutes).
**Treated as `[INFERENCE]`: abstract read via search index, body not re-fetched here.** Wellcome
`works/gc2vxmmr` (Lochner, *Consilia*) is a catalogue stub (title + one Latin line) — too thin for a
`teaches` cell. If the fragment lands on a catalogue record rather than readable body text, that is a
repeat of the r66 "quotable but unsupported" class and should be rejected at review.

### S828 — "Medical amulets, charms and the materia of protection" — DUPLICATE AS SCOPED (HIGH)
- **HIGH — the register this topic names is already owned and already sourced.** The corpus owns
  `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` (danger-to-remedy table §4, healing
  scrolls, healer-as-maker class at :133) and the registry already carries ~30 amulet rows (S600–S651),
  including explicitly *medical* amulets: S609 "The Eye of Providence and the Hamsa in medicine", S636
  Chnoubis amulet, S618 medieval birthing girdle, S622 "Witch-bottles and healing charms", S642 "A history
  of amulets in ten objects", S644/S645 museum amulet guides. Under ACCEPT-C-67 `ONEID` the new entry may
  cite **only** S805–S828 (`foreign` ids are a hard fail), so S828 cannot discharge that prior art by
  reference — it has to carry it, which makes duplication a claim-level, not a stylistic, problem.
- **Genuinely unowned slice (verified):** `grep -rliE "theriac|bezoar|incubat|temple sleep|plague
  treatise|materia medica" corpus/knowledge/` returns only `divination-omen-systems.md` and
  `sacred-topography-pilgrimage.md` (both for incubation), **no theriac/bezoar/materia-medica owner**.
  Rescoping S828 to ingested/pharmacy *materia* of protection (theriac, bezoar, unicorn horn/narwhal) keeps
  the slot honest and non-duplicative.
- **HIGH — the obvious objects are unusable at lands:** SMG `co182417` "Container of theriac" and
  `co106472` "3 small bezoars" are HTTP **429** to direct fetch and have **no wayback snapshot**
  (`archived_snapshots: {}`); a `web.archive.org` capture URL for them would be fabricated bytes. Use a
  source that is readable and archivable (e.g. Cambridge's unicorn-horn feature, which was live in search
  results, or a Wellcome digitised pharmacopoeia page), or reject the row.
- Tier: B for museum object records; theriac's 60–70-ingredient composition claim is a catalogue gloss,
  not a pharmacological finding — `teaches` must say "the catalogue describes", never assert efficacy.

## Findings by severity

1. **HIGH — CAPTURE leg cannot detect a fabricated capture (instrument defect, affects all 24 rows).**
   `reports/round-67/accept-c.py:396-418` only regex-matches the snapshot URL and compares its stripped
   target to the live URL. It never fetches `web.archive.org`. Proven live failure mode: SMG
   `co182417/container-of-theriac` and `co8010533` answer `"archived_snapshots": {}` from
   `archive.org/wayback/available`, yet a row writing
   `https://web.archive.org/web/20261024120000id_/https://collection.sciencemuseumgroup.org.uk/objects/co182417/container-of-theriac`
   passes `CAPTURE` while the snapshot does not exist. This is exactly the "fabricated anchor" class the
   wave is supposed to attack, and it is unreachable from inside the frozen counter.
2. **HIGH — S828 as scoped duplicates an owned register and 30 existing rows, and `ONEID` prevents the
   entry from citing them.** Evidence above. Disposition options, in order: rescope to materia medica
   (verified unowned); or make S828 a first-class rejected row with reason "duplicate of
   myth-symbol/amulets-talismans-apotropaic-marks.md + S600–S651", which also serves R66-D5.
3. **HIGH — S824 conflates sangoma (southern Africa) and nganga (Kongo).** Verified quote supports only
   the sangoma sentence; the lane's own registry uses *nganga* as a Kongo credit (S395/S400/S402).
4. **MEDIUM — capture availability for this batch is poor:** Google Arts & Culture (S824), J-STAGE
   (S826), all SMG object pages (S826 material, S828) have no wayback snapshot. The `no-capture` token
   that would let them through has **zero precedent in 724 rows**; its first use must name a robots/HTTP
   block, not convenience, or the token becomes the round's shortcut.
5. **MEDIUM — S825's UNESCO source does not contain "incubation".** Use UCL/Warwick; keep the entry
   one-way to `divination-omen-systems.md` and `sacred-topography-pilgrimage.md`, which own incubation
   today (line cites above).
6. **MEDIUM — S823's natural 26-word anchor exceeds the lesson's ≤25-word Gate limit**; the 17-word
   verbatim sub-span inside the same sentence is the compliant anchor, and "medieval" is not in that
   sentence.
7. **LOW — tier inflation pressure:** every body I verified is institutional interpretive text or an
   abstract (B), except the J-STAGE paper (A for its own abstract sentence). A-tier claims on object
   records or museum blogs would fail a spot-check of the r66 kind.
8. **LOW — host diversity:** `HOSTS >= 10` is a counter leg over 24 rows; SMG/VAM/Met are already dense
   in the registry (`collections.vam.ac.uk` 18 rows). Six rows on three hosts is not enough on its own.

## Residual risk / verification gaps

- No fragment existed for any of S823–S828 at review time, so quote-in-body verification against the
  *actual* anchors is unperformed; the L1 must re-run steps 1–3 of my contract per fragment.
- S827: no body fetch (declared). S828 theriac/bezoar: bodies unreachable behind HTTP 429; claims about
  their text are `[INFERENCE]` from search-result snippets only.
- Wayback availability is a point-in-time probe (2026-10-24); a row that later triggers a capture will
  legitimately differ. The defect is that the counter cannot tell the difference either way.
- Tool installs: none. No pacman transaction was attempted (host-wide pause respected).

## Report

## Addendum — the C-APPEND vs Ca-D4 id bound (after L1's per-claim lands resolution)

CriticFrontier's alert is arithmetically correct as a *single-tip* reading: `accept-c.py:70` bounds appended ids to
`NEW_IDS ∪ {"S801".."S804"}`, `accept-c.py:357-380` fails any other new id as `extra_ids`, and
`accept-ca.py:226-235` needs `rej_opened_today >= len(R66_REJECTS)+2 = 6` today-dated rejected rows — S801–S804
plus two more, which cannot be S805–S828 because `accept-c.py` ROWS pins all 24 to `status=mined` and ONEID pins
each to exactly one citation. So at a shared tip the two predicates cannot both hold.

L1's per-claim lands separation does resolve it, and I verified the precondition that makes it sound:
**`accept-ca.py` never executes `accept-c.py`** (its `subprocess.run` sites are `git` at :80, the census at :165,
`check-receipt-seq.py --selftest` at :251, `check-gate-quotes.py` at :268). C is therefore measured once, at
`A_c`, where the appended set is exactly S801–S804 + S805–S828.

Residual fragility to carry into closure (not a blocking defect):

1. **C's receipt is valid only at `A_c`.** Both counters use the same whole-file matcher
   (`ROW_RE = r"^\|\s*(S\d+)\s*\|"`, accept-c :73, accept-ca :66), so re-running `accept-c.py` at `A_ca` prints
   `APPEND FAIL … extra=['S829', …]`. Any closure or audit step that re-materializes the tip and re-runs C will
   read that as a regression; post-records topo must pin `A_c` and cite it, never the tip.
2. **Placement cannot absorb the extra rejects.** Putting S829+ under `## Leads` would hide them from neither
   counter (both scan the whole file) and `accept-ca` D2's census exit-0 leg (`:165`) would re-raise E12.

Report: .ufo/waves/round-67/w1/RevSourceSupport4.md

