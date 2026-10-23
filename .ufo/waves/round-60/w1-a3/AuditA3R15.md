NONE-MET

# AuditA3R15 — candidate wording, S647/S648/S649

Scored axis: **depth**. Audit dimensions: verbatim body quotation, support for every clause, source scope, packet-local provenance, and permitted reachability. This is a pre-freeze build audit, not a data-seat verdict or an ACCEPT-D-60 judgment. No control fixture or counter was run.

Inputs: the declared revision-5 claims.json, `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md` (all matching lines), and the working-tree SOURCES.md rows. Each assigned id occurs on exactly one candidate line, with no shared-id line. Ordinary curl GETs reopened each first URL; only the Met challenge was routed to its already-listed Wayback capture. No challenge was passed.

## AUDIT S647 OK

URL: https://openaccess.iku.edu.tr/bitstreams/8b0b8456-e29b-4568-b622-5859e4029189/download

Observed: HTTP **200**, **12,295,670 bytes**, `application/pdf;charset=UTF-8`, 12 PDF pages. SHA-256: `89550b2e3b3b5e670a42656a187c666effb0eb32f327271c46b5079772c7cb22`.

Candidate line 141:

> - Souvenir: as the myth was naturalised, the evil eye bead gained a pervasive use as a souvenir in Turkey (S647). **B**

Registry teaches:

> The evil eye bead has become a pervasive souvenir in Turkey as the myth was naturalised.

Carrying sentence: printed p. 202 / PDF page 10, Conclusions, body paragraph after Figure 11:

> As the result of naturalization of myth, evil eye bead has a pervasive usage as souvenir in Turkey.

This one sentence carries the naturalisation relation, the evil-eye bead, pervasive souvenir use, and Turkey. The candidate and teaches add no stronger cause, date, location, or comparison. The quote is the complete body sentence, not the preceding Figure 11 caption or the CONCLUSION heading. Canonical `to_text` and `locate_in` returned a located quote. No correction needed.

## AUDIT S648 TEACHES

**Minimal packet-local attribution repair; the substantive Pazuzu proposition is supported.**

URL: https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf

Observed: HTTP **200**, **197,505 bytes**, `application/pdf`, five PDF pages. SHA-256: `2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a`; the reopened bytes exactly match L1/captures/S648.bin.

Carrying sentence: page 1, §I Introduction, ordinary body paragraph:

> P. served particularly as the antagonist of the baby-snatching demon →Lamashtu, and was a favourite amulet of pregnant women and young mothers.

The heading identifies P. as Pazuzu. This sentence carries both substantive clauses, including “particularly”, “baby-snatching”, and both groups of women. It is neither a heading nor a caption. Canonical `to_text` and `locate_in` returned a located quote.

Strongest counterexample under the actual reader restriction: **“Heeßel describes” is not established by the packet PDF itself.** Its extracted five-page text has no author byline; rendered opening and closing pages also have none. The PDF `/Author` metadata is `Jürg Eggler`, not Heeßel. Citations of HEEßEL 2002 inside the article are not a byline for this 2007 article. Therefore the current teaches and entry ask a reader confined to the packet URL to accept an author-specific attribution not supplied there.

This is **not an allegation that the bibliographic attribution is false**. An ordinary read of the publisher's separate index, https://www.religionswissenschaft.uzh.ch/idd/prepublication_5.php, identifies “Pazuzu (Nils P. Heeßel)”, links this exact PDF, and gives the same revision date; Heeßel's Heidelberg publication list also identifies the electronic prepublication (https://www.uni-heidelberg.de/md/assyriologie/mitarbeiter/publikationen_hee__el.pdf, p. 4). Those are not S648 packet URLs, so the confined blind reader cannot use them. Do not repair this by adding a separate authority to the packet: neutral attribution is smaller and retains every substantive proposition.

old: - Heeßel describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers (S648).

new: - The IDD article describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers (S648).

Registry teaches old:

> supersedes S602 — Heeßel describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers

Registry teaches new:

> supersedes S602 — The IDD article describes Pazuzu as particularly the antagonist of the baby-snatching demon Lamashtu and as a favourite amulet of pregnant women and young mothers

Keep the source-cell bibliographic author, which the official index corroborates. The repair is confined to the teaches/entry attribution; keep the id, citation, row, quote, and all Pazuzu content.

Round-59 comparison: the spotcheck §3, S602, rejected the universal lead “A protective object is usually aimed:”. That overreach is **gone**, not merely hedged: line 58 now concerns only Pazuzu and its stated use. The separate attribution portability issue above does not revive the old universal.

Impacted axis/dimension: depth / packet-local evidential provenance. Fixable wording defect, not grounds for changing the frozen predicate or accepting an evidential tradeoff.

## AUDIT S649 OK

First URL: https://www.metmuseum.org/art/collection/search/464456

Observed: HTTP **429**, **34,225 bytes**, Vercel Security Checkpoint (`x-vercel-mitigated: challenge`). The live response is not source evidence and was not bypassed.

Listed capture: https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456

Observed: HTTP **200**, **246,282 bytes**, `text/html; charset=utf-8`. SHA-256: `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea`; reopened bytes exactly match L1/captures/S649.bin.

Candidate line 82:

> - The Met's record says hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems (S649). **C**

Registry teaches (prefix removed):

> Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems.

Carrying sentence, visible museum description immediately following the sentences about the Woman with the Issue of Blood and the reverse's orant figure:

> Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems.

The sentence carries the hematite belief, blood flow, favorite-medium characterization, female reproductive health, and menstrual problems. Both entry and teaches preserve “was believed”; neither asserts physiological efficacy. It is description body prose, not the title, image-control text, Public Domain label, navigation, cookie text, or a promo/caption fragment. The anchor is this sentence without its terminal full stop; canonical `to_text`/`locate_in` returned located.

Round-59 comparison: the supplied spotcheck §3 directly details S602 and S623, not S616. The precise S616 rejection is recorded in `corpus/lessons/round-59.md:85`: the added comparison “as much as in its carving”. That comparison is **gone**. Neither candidate line 82 nor S649 teaches ranks the material against carving or any other mechanism. No correction needed. Reachability remains dependent on the listed archive; it worked in this audit and is not guaranteed for later seats.

## Reproduction and scope

- Scratch evidence: `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R15/`: `S647.body`, `S648.body`, `S649-live.body`, `S649.body`, their `.headers`, extracted `.text` files, `S648-page1.png`, `S648-page5.png`, and `audit.py`.
- Quote checks used the lane's `reopen-quote.py` functions on the reopened bytes. For PDFs, direct pypdf 5.4.0 extraction equalled canonical `to_text` exactly for both files. The scratch adapter only put temporary PDFs under this sandbox, inserted `-B` in its Python subprocess, and shortened subprocess timeouts; parsing and matching were unchanged. All three `quote_locates` results were true.
- Dependency used: pypdf **5.4.0**, via `uv run --no-project --quiet --with pypdf==5.4.0`, for the specified PDF extraction. Existing curl, uv, Python, and pdftoppm were used; no host tools were installed or updated.
- All invoked shell commands had timeouts and ran from this seat's scratch directory. The one fetch that the tool automatically backgrounded finished and delivered HTTP 200; no process is left running.
- No lane files other than this assigned report were written. No git/jj writes, data-seat contact, dispatch, counter invocation, acceptance judgment, or runtime invocation occurred.
- This review covers exactly these three ids. It is not evidence that the other 44 ids pass, or that ACCEPT-D-60 passes.
