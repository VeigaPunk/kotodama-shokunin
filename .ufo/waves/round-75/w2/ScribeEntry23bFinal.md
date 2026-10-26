# ScribeEntry23bFinal — final text of the combined amendment `…amend-2026-10-23b.md` (round 75, wave 2)

Seat: scribe, leaf. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. No delegation, no background job, no git/jj mutation.
Nothing installed, nothing upgraded, `pacman` not run. Scratch
`/fast/scratch/hyaku/kotodama-r75/ScribeEntry23bFinal/` created, used, and removed before yield
(the host wiped it once mid-seat; see §7 N8 — everything was re-fetched and re-verified).

Nothing of the round's data has landed and I wrote no product byte: the lane tree is untouched
(`git status --porcelain .ufo/waves/round-75/w2/` shows only `?? .ufo/waves/round-75/w2/`).

## 1. Artifacts

| path (lane-relative) | bytes | sha256 |
|---|---:|---|
| `.ufo/waves/round-75/w2/stage/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md` | 22 947 | `dac22c3e9a78c1089b04eb0d46303c9fefa16fda4c1f9535619a6f5770488e13` |
| `.ufo/waves/round-75/w2/ScribeEntry23bFinal.md` (this report) | — | — |

Staged path = repo-relative path: `stage/corpus/knowledge/myth-symbol/…` lands as
`corpus/knowledge/myth-symbol/…`.

```
$ wc -wc .ufo/waves/round-75/w2/stage/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md
 3779 22947 .ufo/waves/round-75/w2/stage/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md
```

Whole file 3 779 words; body from the first `## ` 3 135 words against the 478-word floor; 7 `## `
sections; header field order `source ×3, verified-at, recheck, ground, topic, gap filled, sources,
couples, scope`; the `- topic:` line is one physical line, 510 characters, no backticks; no header
value matches `<[^>]+>` and no `TODO/TBD/FIXME/XXX/n/a` token appears; no `/tmp` and no `/home`
path anywhere in the file.

Ids cited: **S885, S891, S892 only** — three of the nine lane ids, one per `source:` line, no
campaign-namespace id, no id from outside the nine. `recheck:` carries no id at all.

## 2. What the entry does, and what it refuses

Sections: (1) the article's hierarchy of levels on printed p. 5; (2) the five codes as the Geneva
`Fiche de lecture` of *S/Z* names them; (3) the scholarly relation, in Marrone's own *en partie*
sentence on printed p. 58; (4) an attribution table; (5) a checklist, two decision tables and a
worked non-canonical example; (6) calibration; (7) provenance and the one-window rule.

SimplifierRows' verdict **ADOPT REDUCED** is applied in all four parts:

1. **The "four levels" attribution is cut.** The staged 23b called fonctions/actions/indices/
   informants "the 1966 article's own four levels"; the w1 draft already corrected the article's
   enumeration to three levels. The final text neither prints a four-level list as the article's own
   nor leaves the false phrase lying: §3 states that the four-item list is Marrone's compression,
   that the article's printed p. 6 enumeration is three levels (`fonctions`, `actions`, `narration`,
   each credited) and that `indices`/`informants` are two of four classes of the *functional* level
   on printed p. 11. §6 marks that attribution **discredited as an attribution**.
2. **The S/Z page's French names are used**: `herméneutique`, `sémique`, `symbolique`,
   `proaïrétique`, `gnomique`, with the page's own glosses; the English *semantic*/*cultural* pair
   appears only as the gloss it is, marked as a gloss.
3. **Marrone (S892, printed p. 58) is kept as the account of where the codes sit** — the `en partie`
   sentence, the proairetic synthesis, and his own five spelling variants — and his sentence about
   the list being open questions rather than established results carries §6's calibration.
4. **One evidence window per row**: every S885 quotation below comes from printed p. 5; printed
   pp. 6, 10 and 11 are named as **locators only**, and §7 says so in the file's own words.

Three further corrections were folded in from the refused staged `-23c` and `-2026-10-24`
(the seat's "folded material"): the p. 11 classes, the p. 10 deletion test and the p. 6 three-level
enumeration now sit in the file as locator statements, which is all a single-window row can carry.
The staged 23b's other claims were refused, each for a locatable reason:

| staged claim | disposition |
|---|---|
| "the five codes … a set of simultaneous voices" | refused: the page says the codes are "le lieu de disparition des voix dont est tissé le texte" — where the voices disappear |
| English labels *semantic* / *cultural* as the page's names | refused as names, kept as glosses |
| "the 1966 article's own four levels" | refused; see above |
| S905 / S917 / S919 / S921 as citations | refused as lane ids; re-pointed to S891 / S885 / S891 / S892 |

## 3. Gates actually run

```
$ python3 -B tools/check-cited-lines.py .ufo/waves/round-75/w2/stage/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md
CITED-LINES: 0 finding(s) in 1 file(s)
exit 0
```

Two MULTI-ID findings were found and fixed on the way (a paragraph that named S891 and S892 on one
line, and one that named S891 then S892 on one line); the file's final bytes are clean.

Quotation gate (run twice — before and after the host scratch wipe, with fresh fetches both times):
every double-quoted span in the entry was extracted and counted in the source it claims, after NFKC
and whitespace folding.

```
spans: 47  misses: []
```

Each of the 47 spans occurs **exactly once** in its own document: 22 in the Barthes p. 5
transcription, 18 in the Geneva capture, 7 in Marrone's printed p. 58. The stage directions the
entry gives itself were checked with the same pass: "8 words" (p. 5), "21 words" (p. 5), "17 words"
(S891), "10 words" (p. 58), "30 words" (S892) all match the measured spans; the earlier "11 words"
on the S891 sentence was wrong (it is the sub-span "cinq grands codes…" that is 11 words) and was
corrected to 17.

Also checked in the file's own bytes: header order, one `## ` section minimum, no placeholder token,
no angle-bracket value, and that no physical line carries two distinct S-ids (the lint's own
condition, confirmed independently line by line).

## 4. Fetch record — each User-Agent bound to the response it got (QUALITY 22)

All requests were plain `curl` GETs: **automation: none**, no browser automation, no captcha solved,
no login, no paywall or geo block passed. `curl 8.23.0`, `Python 3.14.8`, `pdftotext 26.08.0`;
nothing installed for this seat.

UA-B = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`
(the round's browser-shaped UA). UA-P = `curl/8.23.0` (the literal default string sent).

| request | UA | HTTP | bytes | sha256 of stored body |
|---|---|---:|---:|---|
| `persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` (notice) | UA-B | 200 | 109 589 | `c2170c1c5b9cc6d6181029d7c2df9688e01aab8243dada8af976ddfda5cb6d1a` |
| `…/page/…_T1_0005_0000` (p. 5) | UA-B | 200 | 4 286 | `8998f55ea7e913d0a82fbed9aacbf312d3fbdb3b1a33066288688c102834fbdf` |
| `…/page/…_T1_0006_0000` (p. 6, locator) | UA-B | 200 | 3 811 | `efee74ba5aaa3723f32e2fe2f983467645d0db3c6db7ec223194c82cd2f0348d` |
| `…/page/…_T1_0010_0000` (p. 10, locator) | UA-B | 200 | 4 320 | `8fe43d677a3cec8689184ec0129763650cebd4bce5b895e5b0b539df6da4fcd4` |
| `…/page/…_T1_0011_0000` (p. 11, locator) | UA-B | 200 | 4 061 | `9cbf7c9485a6683c709a6f94d72d0251f5c746028f5a233b72cadd1ecd885143` |
| `…/page/…_T1_0026_0000` (p. 26, not used) | UA-B | 200 | 4 390 | `fbe16353fb945c97811db21b9f5d414c04f39f0c1be513e67668fe32b356807b` |
| `unige.ch/lettres/framo/cernet/biblio/barth70.html` (live) | UA-B | 200 | 48 045 | `9bccccee0615ce0b3256f4db20880045cfff2106487219082b71f91010b86251` — **challenge body** ("This question is for testing whether you are a human visitor", support ID, no fiche text) |
| same live URL | UA-P | 200 | 245 | "Request Rejected" shell — no fiche text |
| `web.archive.org/web/20041220223357id_/…/barth70.html` (capture used) | UA-B | 200 | 3 898 | `69b5987240ccd7287e4e297f7333be9ed2ceb47a91cf697d196d5cd6b1f2b494` |
| `iris.unipa.it/retrieve/…/2014%20marrone%20age%20dor---2.pdf` (live) | UA-B | 403 | 5 867 | `9756a6d942db4f9ac5b1a5abdf8da132344f009f8245aca23b64ab2df241fa56` |
| same live URL | UA-P | 403 | 5 697 | challenge shell, `cf-mitigated: challenge` (`Just a moment...`) |
| `web.archive.org/web/20251111222249if_/…/2014%20marrone…pdf` (capture used) | UA-B | 200 | 763 802 | `8c0303670ff5db8625d034be958ad5729a2c79fa77f3642efc5f6341fb25a19a` (PDF, 25 pp.; `pdftotext` 73 505 chars) |

Both walls held under both UAs: **challenge met, not passed**. The Geneva page answered a bot
challenge to the browser-shaped UA and an F5 "Request Rejected" shell to the plain one; the Palermo
deposit answered HTTP 403 to both. Each document was then read from the ordinary Internet Archive
capture of the same path, which is why the rows are admitted rather than refused, and the entry
claims nothing about the live pages' present content.

The Persée per-page transcription service is **not** access-controlled: plain GET, HTTP 200, body
text, no challenge and no login, on every page tried. The entry says exactly that; the article-level
`docAsPDF` endpoint was never requested by this seat and the entry makes no claim about it.

**Gate-quote candidates, measured** (the counter's cap is 25 tokens and 80 characters):

| row | candidate | tokens | chars |
|---|---|---:|---:|
| S885 | `aucun niveau ne peut à lui seul produire de sens` | 10 | 48 |
| S891 | `cinq grands codes que vont rejoindre tous les signifiés du texte` | 11 | 64 |
| S892 | `Mais combien, et de quelle nature, sont ces codes ?` | 10 | 51 |

Each occurs exactly once in the stored body named in the table, and each is inside the span the
entry quotes.

## 5. The one-window decision, and what it costs

S885's committed evidence file can hold one fetch, so one page. The seat fixes that page at printed
p. 5, and the entry is built around it: p. 5 carries the concept, the hierarchy rule, the two
relation types, the integration order, the "hierarchy of instances" formulation, the horizontal/
vertical projection rule, and the page's own credits (Benveniste, the Prague School footnote,
rhetoric's *dispositio*/*elocutio*, Lévi-Strauss's mythèmes, Todorov's two grand levels).

Pages 6, 10 and 11 carry the three-level enumeration, the deletion test and the four classes. They
are **named as locators and not quoted**; §7 of the entry states this in the file's own words rather
than leaving a reader to infer it. The consequence the L1 must record: the three-vs-four correction
(§3, §6) rests on a page the window does not hold, so a reviewer reading only `evidence/S885.txt`
cannot re-locate it. That is the honest price of one row per document; the alternative SimplifierRows
offered (p. 6 as the anchor) is ruled out by this seat's window instruction.

Measured: the p. 5 extracted visible body is **3 811 characters**, under the 4 096 floor, so the
EVIDENCE leg's `window-scope: whole-document` branch is available for S885 with
`visible-chars: 3811`; the S891 capture body (2 194 visible characters of text after tag stripping)
is likewise under the floor, and the S892 window must be the p. 58 page extract (`excerpt`).

## 6. Disposition of RevEntryQuality's findings F1–F13

The review file my seat prompt names as `.ufo/waves/round-75/w1/RevEntryQuality.md` does not exist
under the lane; the completed review is at the **fleet** path
`/home/vgpnk/Projects/shokunin/.ufo/waves/round-75/w1/RevEntryQuality.md` (see §7 N1). Read there.

| # | applied to this file? | what was done |
|---|---|---|
| F1 campaign IDs | **yes** | no campaign id is cited; the Barthes document is cited as S885, never as S744/S763, and no round chronology survives in prose |
| F2 S870 | **n/a** | this file never cites S870 |
| F3 criterion-15 shape | **yes** | final bytes print `CITED-LINES: 0 finding(s)`, exit 0; two multi-id lines found and split |
| F4 fold vs one window | **yes, in the seat's direction** | quotes restricted to p. 5; pp. 6/10/11 named as locators and explicitly not quoted; the deferral is stated in §7 of the entry |
| F5 dangling `couples:` | **yes** | couples name only files that exist at base (`myth-symbol/comparative-frameworks.md`, `synthesis/worldbible-integration-contract.md`) or land in the same claim-C landing (`narrative-structure-frameworks.md`, `…amend-2026-10-23.md`); the pending `era-periodization-models.amend-2026-10-23b.md` target is **not** named |
| F6 four classes as four levels | **yes** | cut; §3 and §6 state the three-level / four-class distinction and refuse the phrase |
| F7 row ↔ used-by | **yes, for S891/S892** | the entry cites both rows, so their `used-by` is non-empty exactly as the ROWS leg wants; the row-set question itself is the L1's |
| F8 calibration absent | **yes** | §6 names mainstream-as-method / contested / discredited-as-attribution, each with its reason and its page |
| F9 "independently" | **n/a here** | the claim belongs to the base entry; this file makes no independence claim |
| F10 campaign pointers | **yes** | no `CANNOT-ANSWER.md` or `SOURCES-PROPOSED.md` pointer; `ground:` states the durable base-state gap with the commit and the equation |
| F11 not usable | **yes** | §5 ships a six-item ordered checklist, two decision tables and a worked non-canonical example; §4 ships an attribution table |
| F12 uncited Eco/Bremond | **n/a** | only the names the article itself credits on p. 6 appear, and they appear as its credits |
| F13 wall disposition unstated | **yes** | §7 states both walls as met and not passed, names the capture used, and binds each UA to its own response in this report |

## 7. Findings for the L1 (new in this seat)

**N1 — the w1 review named by the seat prompt is not under the lane.** `RevEntryQuality.md` exists
only at `/home/vgpnk/Projects/shokunin/.ufo/waves/round-75/w1/`; `.ufo/waves/round-75/w1/` in the
lane holds no such file, while lane `w1-results.json` records the report as
`.ufo/waves/round-75/w1/RevEntryQuality.md`. Path resolution for wave-2 prompts should say which
root. I read the fleet copy; no file was written there.

**N2 — the README draft's third-row topic is stale.** `drafts/readme-rows.md` §2.3a carries a topic
string for this file ("the 1966 article's own three levels and its four classes …"). The final topic
is different because the entry was reduced (one window; French names; Marrone as the relation).
The exact string to bind is §8 below; `sweep.py`'s `topic_of()` binding (the draft's §4.2) will
re-derive it, so no row may be copied from §2.3a as-is.

**N3 — S885's window is shared with a sibling entry that quotes p. 26.**
`drafts/narrative-structure-frameworks.amend-2026-10-23.md` §3 quotes the p. 26 spans ("la dystaxie
oriente une lecture « horizontale »…", "très souvent une même unité peut avoir deux corrélats…"). If
S885's committed window is p. 5, those quotations in that file rest on a page the window does not
hold, exactly the class SimplifierRows §4 describes. Either that entry is re-pointed to p. 5 for its
S885 quotes, or the L1 accepts that its p. 26 spans are unbacked — the counter's EVIDENCE leg checks
only the Gate quote, so this is review-visible only. Flagged, not edited: it is not my file.

**N4 — the same Wayback capture URL returns different wrapper bodies.** Two fetches of
`…/20041220223357id_/…/barth70.html` in this seat gave 5 693 B (`5ab82216…`) and 3 898 B
(`69b59872…`, identical to the w1 ScribeEntryAmend record); both carry the same fiche text and all
18 S891 spans locate in both. The evidence file's sha256 must therefore be of the **stored** body,
and a re-opener must not be promised a byte count. The Marrone capture is stable
(`8c030367…`, 763 802 B, three seats agree).

**N5 — the p. 5 window can use the whole-document branch.** Extracted visible body 3 811 characters
< 4 096; declared as `window-scope: whole-document` with `visible-chars: 3811` it satisfies the
EVIDENCE leg without an arbitrary excerpt boundary.

**N6 — Marrone's printed page 58 is PDF page 7.** `pdftotext -f 7 -l 7` puts the header `58` on the
first line and carries every S892 quote in this entry. The row says "PDF p. 7 of 25"; that is
consistent and is reconfirmed here, so a re-opener must slice the PDF at page 7 rather than search
page 58.

**N7 — the w1 scribe's "do not land this round" note is superseded.** `w1/ScribeEntryAmend.md` §1
and §6.2 say the `-23b` file must not enter `corpus/knowledge/` because claim C's frozen `entries`
list named two paths. The `claims.json` dispatched to wave 2 lists **three** entries, this path
included, and SimplifierRows §2.3 recommends exactly that. As it stands the file is inside the
graded set, so the ENTRIES/REPOINTED/INDEX legs will demand it: it must land, and the README needs
its third row, the myth-symbol heading `(32)` and footer `252`.

**N8 — the host wiped this seat's scratch mid-run.** At 16:55 the scratch root was emptied by
something outside this seat; my fetched bodies vanished. Everything citable here was re-fetched in a
fresh scratch dir and re-verified: the five Barthes pages came back **byte-identical** (same five
sha256s), the Marrone capture byte-identical, the Geneva capture with the variant in N4. The
47-span check above is the re-run, not the earlier one.

## 8. The `- topic:` line, verbatim (for the README row)

```
- topic: where Barthes's five codes sit — the five codes in the S/Z reading sheet's own French names (herméneutique, sémique, symbolique, proaïrétique, gnomique); a semiotician's statement that they are in part a reformulation of the levels of the 1966 Introduction, with the proairetic code a synthesis of two of those levels; and the 1966 article's own hierarchy of levels of description on the one page this file can quote — with the attribution table and the design orders that follow from it, as method, not canon.
```

One physical line, 510 characters, no backticks, so it drops straight into the
`` - `narrative-structure-frameworks.amend-2026-10-23b.md` — `` prefix. It sorts between
`…amend-2026-10-23.md` and `narrative-structure-frameworks.md`.

## 9. Out of scope for this seat — not done, not claimed

Registry rows and their cells; `used-by`; the id-renumber map; Gate records; evidence windows; the
README rows, headings and footer; the lesson; claims/ledger edits; counters, controls, fixtures;
commits. No file outside the staged entry and this report was created, modified or deleted; the
lane's git/jj state and index were only read. `shokuknow` was read, never written.

Not run: the acceptance counters (they grade `<lands>`, which does not exist), the Persée
`docAsPDF` endpoint, and any check of the other six entries' bytes.

## 10. Tooling record

No tool installed, no tool upgraded, no `pacman` (paused host-wide). Used: `curl 8.23.0`,
`python3 3.14.8`, `pdftotext 26.08.0`, `wc`, `sha256sum`, and the lane's
`tools/check-cited-lines.py`.
