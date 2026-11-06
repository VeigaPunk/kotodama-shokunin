# ExecRegistry99 — dropped candidates

ScoutSources99 opened 14 candidates; 11 became rows S1007–S1017. The three not written,
with the measured reason and the exact response:

| key | url | attempt | result | disposition |
|---|---|---|---|---|
| C6 | https://www.iranicaonline.org/articles/courts-and-courtiers-x/ | 1 (this seat) | HTTP 403, 5539-byte Cloudflare "Just a moment..." shell | UNREACHABLE — bot challenge is a wall, not a transient failure; no bypass attempted. Flip: an open mirror of the same entry or a peer-reviewed article on Persian madh/qasida panegyric. |
| C8 | https://skaldic.org/m.php?p=text&v=intro&i=1258 | 4 (this seat: 1 + 3 retries) | curl rc=28, connect timeout after 30 s, 0 bytes each | UNREACHABLE — transient class, retried 3x with 20 s backoff, every attempt recorded. Flip: the database answers from this host, or the printed SkP volume text is available. Covered instead by S1016 (Potts, ASNC). |
| C14 | https://journal.ru.ac.za/index.php/africanmusic/article/download/1116/591/593 | 1 (this seat) | HTTP 200, 1441621-byte PDF | REJECTED on anchor scope, not on access: Gourlay's article is about long trumpets of northern Nigeria and the praise-singer patronage passage is a six-line aside, so a row scoped to praise poetry would be mis-anchored. Quote verified count 1; kept out of the registry. Flip: a dedicated study of Hausa maroka praise-singing and patron exchange opened at source. |

Notes:

- C1's OpenEdition chapter page (https://books.openedition.org/obp/1192) served only a preview and the
  OBP chapter page returned HTTP 429 on three scout attempts; the row's URL is the Internet Archive
  copy of the same CC BY edition, which is what the quote is counted in and what this seat re-fetched
  (HTTP 200, 1431723 bytes, sha256 73df25c214bd03c2a36784c9d7faef3adaeb265b8ef1a7566713493a09f892b8).
- C10's archive.org stream page returned 184993 bytes to this seat against the scout's 191267-byte
  capture; the quote counts 1 in both the shipped capture and the fresh bytes, so the row stands and
  the byte difference is recorded in rows.md.
