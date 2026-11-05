# Smallest corrections per survivor (CriticClaims92, not applied)

Frozen tool sha256 905be2fe…; no file in the repo was edited. Each correction is the smallest
change that would make the named counterfeit refuse, with its tradeoff. None is run here; each
needs a mutant in reports/round-92/mutants.py before it is trusted.

## A1 — chrome quote as own sentence + forged manifest quote (rc 0)
Gap: GATE binds the quote to `max(overlap(quote, teaches), overlap(quote, manifest.quote))`. The manifest quote is writer-asserted, so a forger writes it to share 3 words with the chrome.
Correction: (a) refuse a gate quote that occurs verbatim as a sentence of the entry body (self-quote into prose); (b) require the manifest quote to itself occur in the capture bytes and to overlap the teaching cell by ≥3 words, so the manifest cannot bind to chrome alone.
Tradeoff: (b) still trusts the teaching cell; chrome that the teaching cell also names passes. State in bounds.

## A2c–A2f — url variants shadow a base row (rc 0)
Gap: `norm_url` lowercases scheme and host, drops `#fragment`, default ports and trailing slashes. It keeps the scheme, `www.`, the query and the path case, so `http://` vs `https://`, `www.`, `?ref=` and `/Base-Prayer-Notes` are distinct strings.
Correction: in `norm_url`, also drop a leading `www.`, map `http`→`https`, drop the query string, and casefold the path; then the existing UNIQUENESS shadow check applies unchanged.
Tradeoff: a registry that serves distinct content at a path-case or query variant would be refused as a shadow; flag rather than refuse if the operator wants that. Scheme/www/query are the safe part.

## A2b — uppercase scheme (refused, but UNIQUENESS is blind)
Not a survivor. `URL_RE` is `https?://` and case-sensitive, so `HTTPS://` yields no url and the shadow leg never sees it. CAPTURE (`row carries no URL`) and GATE refuse it instead. Correction: compile `URL_RE` with `re.I` so UNIQUENESS sees the url too; the refusal then names the right leg.

## A3b — capture is the graded entry plus one newline (rc 0)
Gap: the byte-copy guard compares sha256 of the capture with the graded files' sha256 (`graded_shas`). One added byte changes the sha, and the normalized text is unchanged.
Correction: compare `norm(capture)` with `norm(graded)` for every graded file, and refuse when they are equal or when the capture's normalized text is a substring of a graded file.
Tradeoff: a capture that quotes a large part of a graded file would be refused on the substring arm; use equality only if that is too strict.

## A4a — three one-phrase headings + a table header (rc 0)
Gap: TOPIC counts phrase anchors over headings and table rows and needs span ≥3 surfaces. A heading of one word ("## address") counts as a full surface.
Correction: count a heading as an anchor surface only if it has ≥3 words and at least one content word beyond the phrase; or require ≥2 anchored phrases per counted surface.
Tradeoff: short legitimate headings would be uncounted; they then need prose anchors instead.

## A5d / A5e / A5f — disposition hidden by markdown, table or zero-width form (rc 0; under-fire)
Gap: `dispositions()` matches `DISPO_RE` against `line.strip()` with an optional `[>\-*+\s]*\s` prefix. `**S001** LOCATED`, `| S001 | LOCATED |` and `LOC\u200bATED` never match, so an old id can gain a visible LOCATED move that APPENDONLY does not see.
Correction: before matching, remove markdown emphasis and code marks (`*`, `_`, backtick), table pipes, and Unicode category Cf characters (`unicodedata.category(c) == 'Cf'`), then match. Add 5d/5e/5f as mutants in reports/round-92/mutants.py.
Tradeoff: stripping `*` and `_` could merge two words; keep the stripped copy only for matching, not for the quote check.

## A5b — prose "S001 located in the archive" refused (over-fire, by design)
Not a survivor; recorded because the question was over-fire vs under-fire. The relaxed anchor refuses honest prose that starts with an old id, contains "located", and has no base disposition for that id. A5a shows no over-fire when the base disposition is LOCATED (no movement, clean). Both answers hold: over-fire for undisposed old ids, under-fire for the wrapped forms of A5d–A5f. Correction, if wanted: only refuse a line that also carries an `accessed <date>` token, which costs the V10a discrimination the round needs. Keep the conservative refusal and document it in bounds.

## A6a / A6b — base row rewritten or dropped in the lands registry (rc 0 in the tool)
Gap: the entry mode does not compare lands base rows with the base registry; only advance mode does (OTHERCELLS). The frozen counter does: `reports/round-92/measure92.py` lines 303–310 compare every base row (`removed` / `cells changed`) for claim C. So the claim-level gate refuses these; the entry tool alone does not.
Correction (tool-level, defence in depth): in `grade_entry`, for every base row id, refuse if the lands row is absent or its cells differ from the base row cells (names leg e.g. OTHERCELLS). Mutants: rewrite one teaches cell; delete one base row.

## A6c — capture is an in-root symlink to a non-graded blob (rc 0)
Gap: `capture_error` checks the manifest path lexically (no `..`, under the capture dir) and then opens `os.path.join(root, rel)`, which follows symlinks. The sha check is against the target, and the graded-bytes guard covers only the graded files. This is the residual of routed finding 6 (base-lesson, README-like non-graded blobs).
Correction: refuse `os.path.islink(path)` for any capture; resolve `os.path.realpath` and require it to be a regular file inside `realpath(root/capture_dir)`. Add base-lesson, corpus/README.md and claims-like files to the graded list.

## A6d — capture is a symlink escaping the repository root (rc 0)
Gap: same as A6c. Lexical confinement only.
Correction: the realpath-confinement and islink refusal of A6c. Mutant: symlink to a host file outside the root.

## A6e — quote exists only in raw HTML markup (rc 0)
Gap: CAPTURE checks `norm(quote)` in the normalized raw bytes, so a quote inside `<meta content>`, `<script>` or an attribute passes as "located prose".
Correction: when the capture looks like HTML (leading `<` or `<html`), strip `<script>`, `<style>`, `<head>` and all tags (stdlib `html.parser`), then require the quote in the visible text.
Tradeoff: a quote split across an inline tag would be refused; acceptable, since the located quote should be visible text.

## A6f — decoy first quote, chrome second quote (rc 0)
Gap: `gate_quotes` takes only `QUOTE_RE.search(line)` (the first span). A second, chrome, "body:" quote in the same line is never checked.
Correction: check every quoted span on the gate line for the capture and bound tests (each must occur in the capture, and each must bind to teaching/manifest). Tradeoff: a line with two legitimate quotes must have both bound.

## A6g — manifest with rows as a list (rc 1, unnamed traceback)
Not a survivor; an operability defect. `man.get('rows', man)` is a list, `man_rows.get` raises AttributeError, and the process exits 1 with a traceback and no named FAIL leg. Correction: type-check `rows` as a dict keyed by id and refuse with a named leg (MANIFEST). The same class exists for any uncaught exception in grade_entry (only `Refused` is caught, at line 1251).
