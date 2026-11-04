# ScoutSourcesWitch — round 84, wave 1 (claim D recon)

Independent second reading of the four claim-D candidates. Every URL was opened by ordinary plain HTTP GET on
2026-11-04, in two request shapes, and hashed. Row-level evidence is in
`.ufo/waves/round-84/w1/stage/ScoutSourcesWitch/S914.txt` through `S917.txt`, with the synthesis in
`.ufo/waves/round-84/w1/stage/ScoutSourcesWitch/second-reading.md`.

## 1. Headline: the brief's S915 premise is wrong in a way that changes the rejection reason

The L1's correction says the Sorcery page serves "only the Wikisource page header plus a Proofreadpage
transclusion template — no article body". That is not what the bytes say. The article body is present, complete
and un-truncated; it is 452 characters and **71 words**:

> SORCERY, magic, enchantment, witchcraft; the use of supposed supernatural powers by the agency of evil spirits
> called forth by spells, incantations, &c., on the part of the magician, sorcerer or witch. The word meant
> originally divination by means of the casting or drawing of lots, and is derived from the O. Fr. sorcerie,
> sorcier, a sorcerer, Med. Lat. sortiarius, one who practises divination by lots, sortes (see Magic,
> Divination and Witchcraft).

The "no body" impression comes from a stripper artefact, not from the page: the served HTML injects the
unexpanded Proofreadpage payload as literal JSON at the transclusion point, mid-word after "sorci", and the
first clause also carries `</b>` and `&amp;c.` inside it. Strip the payload spans and the body is there. The
proofread page at `Page:EB1911 - Volume 25.djvu/447` carries the same 71 words at pagequality level 1.

So the rejection stands, but for the right reason: the article is a **printed stub** — a single definitional
sentence with a cross-reference — not a damaged transcription. It contains zero institutional content:
case-insensitive substring counts over the 71-word body are accus 0, trial 0, tortur 0, confess 0, evidenc 0,
punish 0, law 0, court 0, judic 0, witness 0, slander 0, heresy 0, inquisit 0. A row built on it could not
supply the procedure/accusation quote claim D requires, and could not support four of the six scopes.

This matters for the record: "the page did not serve its text" is a platform claim and a future reader can
disprove it in one GET. "The article is a 71-word definition" is a source claim and is true.

## 2. Substitute verified (the L1's pointer, re-opened independently)

**S915 → Howard Williams, *The Superstitions of Witchcraft* (1865), Project Gutenberg #22822.**
HTTP 200 in both request shapes, 450,230 bytes both times, sha256
`884075101bb1ce9d975faff86d09a6a9851c46560e966ca75d8038b050c003c4` both times, 71,246 words, 1865 Longman
title page, release date 2007-10-01. Two quotes located and counted:

- Part II ch. v, paragraph opening "Previously to the 'Witch Act'": the statute detached sorcery from the
  political indictment it used to ride on. 25-word excerpt, live ws 1 / fold 1, capture ws 1 / fold 1.
- Same chapter, the Gilles Garnier case (Dole, 18 January 1573): fifty witnesses, the rack, "an unreserved
  confession", then the sentence printed verbatim. 19-word excerpt, live ws 1 / fold 1, capture ws 1 / fold 1.

Also checked and measured, and recorded here as a **named spare only — not used this round** (L1 instruction,
2026-11-04): **King James VI, *Daemonologie* (1597), Gutenberg #25929** — Book II ch. vi carries both the
interrogation rule and the two "helpes" for trial (the mark, the water). Stronger on proof technology, but Early
Modern spelling and a whole-book swap; Williams stays the S915 row.

**S916 → anchor on the Bull, not the root.** Confirmed independently. The root page is 216,384 bytes and 2,174
words of front matter and contents, with `Template:Incomplete` rendered; `/Part_I`, `/Part_I/Question_I` and
`/Part_III` all 404. The Bull page is 73,365 bytes, sha256
`cc7b7d31bf089db6df181e1b347daf785736056885b4971352034e40f035b322`, transcluded from djvu pages 52-54, printed
pp. xliii-xlv, all three pages at pagequality level 3. That page is the citable text for the vocabulary set, the
delegated jurisdiction and the no-appeal clause.

One structural gift worth using: the root page's CONTENTS is a complete procedural schema — Part III's 35
Questions under three heads, the judge's Eleven Actions, pages 194-271, from "The Method of Initiating a
Process" to "Of the Number of the Witnesses" to "Whether Mortal Enemies may be Admitted as Witnesses" to "the
Place of Detention and Torture" to the seven forms of sentence and the appeal. That is the accusation grammar
as an attested outline, and it is on the root URL even though the questions themselves are not.

## 3. Verdicts

- **S914** EB11 "Witchcraft": usable, strongest for the institutional thesis and the confession clause. 4,458
  words, 98,968 bytes, sha256 `68511af9...0ef4`, revision 15556864.
- **S915** EB11 "Sorcery": rejected (71-word stub). Substitute Williams #22822: usable.
- **S916** Malleus, Summers 1928: usable on the Bull; the root is a cover page and must not be cited as text.
- **S917** Upham, *Salem Witchcraft*: usable, widest scope coverage. 1,801,648 bytes, sha256 `925e3634...9539`,
  release 2006-02-24, updated 2021-10-15, 1,051 `[i.N]`/`[ii.N]` page markers.

Coverage across the six scopes: S914 five of six; S917 four; Williams four; the Bull two (but uniquely the
vocabulary list and the jurisdiction). Only the union covers all six. No row supplies the Malleus' own
interrogation text, the statute text itself, or a non-European comparison.

## 4. Quotes the entry can use, with the counts a checker will recompute

All counts are exact-substring occurrences; "ws" collapses whitespace, "fold" adds case, typographic and
diacritic folding. Every listed span is unique: ws 1 / fold 1 on the cited URL.

- S914 p. 755 — "the modern idea of witchcraft is largely a learned product—the result of scholastic and
  inquisitorial ingenuity" (16 words). The institution as a *learned fusion*.
- S914 p. 757 — "they plied their tortured victims with questions and were able to extract such confessions as
  they desired" (17). The proof engine, and it names the 1484 Bull that S916 carries.
- S914 p. 756 — "for the civil law it was a violation of the civil rights of others, so far as real results were
  produced" (21). The church/secular split.
- Williams pp. 168-185 — "Previously to the 'Witch Act,' the charge of sorcery was, in most cases, a
  subordinate and subsidiary one, attached to various political or other indictments" (25).
- Williams pp. 168-185 — "Fifty persons were found to bear witness; and he was put to the rack, which elicited
  an unreserved confession" (19).
- Bull p. xliii — "many persons of both sexes, unmindful of their own salvation and straying from the Catholic
  Faith, have abandoned themselves to devils, incubi and succubi" (24).
- Bull p. xliv — "We decree and enjoin that the aforesaid Inquisitors be empowered to proceed to the just
  correction, imprisonment, and punishment of any persons" (22).
- Bull p. xlv — "with excommunication, suspension, interdict, and yet more terrible penalties, censures, and
  punishment, as may seem good to him, and that without any right of appeal" (25).
- Upham i.414 — "By the laws of all nations, Catholic and Protestant alike, in the old country and in the new,
  it was treated as a capital offence" (25).
- Upham ii.251 — "It was concluded best to appoint a special court of Oyer and Terminer for the witchcraft
  trials" (17), with the same-page "A shade of illegality rests upon the very existence of this special court."
- Upham ii.452 — "having taken testimony from the Devil himself, through witnesses who swore to what they said
  the Devil communicated to them" (20).
- Upham i.433 — "he commenced actions in the County Court for defamation against his accusers" (12), and the
  verdict Upham prints next: the jury finds for the plaintiff, "2d damage & cost of Court 29sh., yet
  notwithstanding doe conceiue, that by the testmonyes he is rendred suspicious."

## 5. Constraints the row and entry authors must not trip

These come from reading the lane's own graders, not from guesswork:

- `tools/check-cited-lines.py` flags **TABLE-ID**: *any* line whose first non-space character is `|` and which
  carries an S-id. Claim D requires `tools/check-cited-lines.py` = 0 findings, and it also requires >= 20
  anchors each carrying exactly one S-id. Therefore the `## 4. Attested anchors` block **must not be a Markdown
  table** — write it as bullets or paragraphs, one and only one S-id per line. The same rule means `## 2. The
  decision table` rows must carry no S-ids at all; put the ids in the anchors block and in the prose.
- `tools/check-cited-lines.py` is run on **the entry file alone**, not on a tree: round 83's own gate row reads
  `python3 -B tools/check-cited-lines.py corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md` and
  expects `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0 (`.ufo/waves/round-83/w1/ScribeEntry.md`). A
  directory argument would walk only `.md` files, so the `.txt` receipts here are outside its reach either way.
- `tools/check-cited-lines.py` also flags **MULTI-ID** (two or more distinct S-ids on one line), so no anchor
  line may cite two sources "for one sentence".
- `tools/check-cited-records.py` flags any absolute temporary-directory path (the three usual roots) in a round
  document, and any backticked `reports|corpus|tools|.ufo` path that resolves to a zero-byte file. Cite
  repo-relative paths, and only paths that carry content.
- `tools/check-source-access.py` flags bypass markers in the source, anchor and teaches cells and then requires
  the row to be `rejected`. Keep the cells to plain fetch facts: URL, HTTP status, bytes, sha256, capture. The
  drafts in the receipts are already clean against that regex.
- The row contract is eleven cells with no `|` inside any cell. Every URL, every sha256 and every locator above
  is written without a pipe; the em dashes and the en dash in "pp. 168-185" are safe, but a URI containing
  `|` is not.

## 6. Counts and where they came from

- Quotes were counted on three substrates where available: the served bytes, the extracted visible text, and
  the proofread `Page:` wikitext (S914 pages 776-779, S915 page 447, S916 pages 52-54). Agreement across all
  three is what makes a span safe to lift.
- Raw-substring counts on HTML are usually 0 even for a verbatim span: line wrapping, `</b>` mid-clause,
  `&amp;c.`, and `&nbsp;` all break an exact match. "ws" and "fold" are the honest measures there; the receipts
  give raw, ws and fold side by side so a stricter checker can be read against the same numbers.
- Wayback: the availability API returned 429 for every URL; the CDX endpoint answered 200 for all. S916's Bull
  URL has no capture at all. S914's only capture (2008) predates the transcription and does not contain the
  quoted text. S917's capture is body-identical (all 60 diff hunks in header/footer) and carries every quoted
  span. Williams' capture carries both spans but is not byte-identical.

## 7. Remaining unknowns

- Whether the round wants a fifth row for the statute text itself (1604 c. 12, or the 1736 repeal). Williams and
  Upham both describe it; neither prints it, and no row in this set can quote an enacting clause.
- S915 is **settled**: Williams #22822 is the row (L1, 2026-11-04). Daemonologie #25929 stays a named spare,
  measured but unused this round. No further sourcing decision is open on that row.
- Tier for S914: the round-83 precedent for an EB1911 article (S910, "Marriage") was A, but this article is
  synthesis-heavy and quotes nothing directly except the Malleus's title. That is the L1's call; the receipt
  records the facts it needs either way.
