# Gate — claim-D registry rows S914–S918

Every row below was opened by plain HTTP GET on 2026-11-04 with the UA
`kotodama-scribe/1.0`; receipts are the four `S91*.txt` files in
`.ufo/waves/round-84/w1/stage/ScribeRowsWitch/`. URLs, access dates,
locators and the verbatim located quote are given per row (QUALITY 31
(iii)); raw/folded counts are against the served bytes, where raw counts
the exact quote in the byte stream and folded counts it after tag
stripping and whitespace collapsing.

- **ADMITTED — S914, EB11 "Witchcraft" (N. W. Thomas), tier B.**
  `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Witchcraft`,
  accessed 2026-11-04 (HTTP 200, 98968 bytes, sha256 `68511af97aaf96f3abaadfcd85af0a9ef2dff0a93cb32c49e2041a14140a0ef4`;
  revision 15556864; Wayback capture 2026-01-29, HTTP 200, 86021 decoded
  bytes, the quote present once, not byte-identical to live because the
  capture is an earlier Parsoid render). Locator: pp. 755–758, section
  "Further Development", p. 758. Located quote, 18 words: 「by a strange
  perversion these admissions, wrung from their victims by rack or
  thumb-screw, were described as voluntary」 raw 0 / folded 1 (line wrap).
  Calibration: the article is dated 1911 and ends at the "Psychology of
  Witchcraft" section; it does **not** mention the 1735 repeal, so the
  entry's repeal sentence must not cite this row.
- **ADMITTED — S915, Howard Williams, *The Superstitions of Witchcraft*,
  tier B.** `https://www.gutenberg.org/cache/epub/22822/pg22822.txt`,
  accessed 2026-11-04 (HTTP 200, 450230 bytes, sha256
  `884075101bb1ce9d975faff86d09a6a9851c46560e966ca75d8038b050c003c4`;
  eBook #22822, release 2007-10-01; Wayback capture 2026-09-29, HTTP 200,
  450230 decoded bytes, sha256 identical — byte-identical). Locator: Part
  III, ch. I ("The Bull of Innocent VIII"), the paragraph containing "The
  third part, which contains the Criminal Code" (the Ennemoser abstract).
  Located quote, 19 words:
  「The arrest might take place on the simple rumour of a witch being found
  somewhere, without any previous denunciation.」 raw 0 / folded 1 (CRLF
  line wrap). Calibration: the chapter quotes Ennemoser's abstract at
  second hand; the rule detail is a lead back to the 1489 text, not an
  independent witness to it.
- **ADMITTED — S916, the Bull of Innocent VIII (1484), tier A.**
  `https://en.wikisource.org/wiki/Malleus_Maleficarum/The_Bull_of_Innocent_VIII`,
  accessed 2026-11-04 (HTTP 200, 73365 bytes, sha256
  `cc7b7d31bf089db6df181e1b347daf785736056885b4971352034e40f035b322`;
  revision 14260824). Locator: "The Bull of Innocent VIII", p. xlv, the
  empowerment clause. Located quote, 17 words: 「the aforesaid Inquisitors
  be empowered to proceed to the just correction, imprisonment, and
  punishment of any persons」 raw 1 / folded 1. No archive capture exists:
  the CDX exact query returned no rows at all (probed 2026-11-04), so the
  live read is the only copy. Calibration: the translation is Summers's,
  reprinted from *The Geography of Witchcraft* pp. 533–6 (Kegan Paul),
  and the Malleus landing page (HTTP 200, 216384 bytes) carries only front
  matter and contents — the treatise body is not transcribed on
  Wikisource (probed `Malleus_Maleficarum/Question_1` etc.: HTTP 404), so
  this row's scope stops at the warrant, not the trial procedure.
- **ADMITTED — S917, Upham, *Salem Witchcraft*, tier B.**
  `https://www.gutenberg.org/cache/epub/17845/pg17845.txt`, accessed
  2026-11-04 (HTTP 200, 1801648 bytes, sha256
  `925e3634e0226c4a5378595edccbfbb4386471678c5d5b688784be085aa09539`;
  eBook #17845, release 2006-02-24, updated 2021-10-15; Wayback capture
  2026-09-05, HTTP 200, 1801648 decoded bytes, sha256 identical —
  byte-identical). Locator: vol. I, part second ("Witchcraft"), p. 433,
  the John Godfrey defamation actions of 1659. Located quote, 14 words:
  「soon after, he commenced actions in the County Court for defamation
  against his accusers」 raw 0 / folded 1 (line wrap). Calibration: 1867
  antiquarian narrative printing court documents in old spelling; the
  documents are selected and framed by Upham, so quote them as his
  transcription.
- **REJECTED — S918, EB11 "Sorcery", tier C.** The S915 candidate is kept
  as its own rejection row. `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Sorcery`,
  accessed 2026-11-04 (HTTP 200, 60730 bytes, sha256
  `2c4092db343fa6274f3f5edccbb72016cf5e9ead485fd7024b3fc83644a84726`;
  revision 11974381; the one 2026 Wayback capture, 20260114084233, HTTP 200,
  54804 decoded bytes, carries the paragraph with the headword cased
  "Sorcery" — an older render, not byte-identical, so no capture claim is
  made for the span). Locator: p. 431 (proofread page djvu 447), the
  article's single printed paragraph. Located quote, 21 words: 「SORCERY,
  magic, enchantment, witchcraft; the use of supposed supernatural powers
  by the agency of evil spirits called forth by spells, incantations」
  raw 0 / folded 1 (the headword is split by an inline `<b>` tag). Reason
  of record: the printed article is a 71-word dictionary stub, definition
  only — zero accusation, trial, torture, evidence or law vocabulary.
  Flip: a full EB11 article body transcribed at the same URL. The earlier
  premise that the page serves no body at all was a stripper artefact (L1
  accepted, 2026-11-04); the body is served, so the rejection rests on the
  stub's content, not on unquotability.
