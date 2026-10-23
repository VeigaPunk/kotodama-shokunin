#!/usr/bin/env python3
"""Generate the round-63 single v2 wave spec (build + attack together) for kotodama.

Usage (lane root): python3 -B .ufo/waves/round-63/gen-w1.py
Writes .ufo/waves/round-63/w1-spec.json. 69 seats; attack roles (reviewer 29,
mutation-tester 8, critic 1) = 38/69 = 55% >= 25%.
"""
import json
import pathlib

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
SCR = "/fast/scratch/hyaku/kotodama-r63"
REV = "80d53ffde7788299b69dbb0bd0436b2b7ddddb95"
BASE = "65b393ef3a4d82bd693cc21b7f96a1231417d522"
SHA_O = "a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de"
SHA_C = "3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca"
GOD = pathlib.Path.home().joinpath(".agents/skills/godspeed/directive.md").read_text()
LEAD = "/skill:godspeed\n" + GOD + "\n"
ENTRY = "corpus/knowledge/culture-material/headgear-head-covering-codes.md"

CONTEXT = f"""# Goal
Kotodama round 63 (hyaku run 5, 2026-10-23 UTC), SINGLE WAVE: build + attack together. Lane repo {LANE} (branch main, jj-colocated), revision `{REV}` (the freeze; round base `{BASE}`). Read first: {LANE}/reports/round-63/claims.json (both frozen predicates), the docstrings of {LANE}/reports/round-63/accept-o.py (sha256 {SHA_O}) and {LANE}/reports/round-63/accept-c.py (sha256 {SHA_C}), and {LANE}/corpus/lessons/round-62-verifier-spotcheck.md section 5 (the routed defects this round closes). Two claims, each ONE frozen predicate:
- O (operability, capability repair, GATING): repair {LANE}/tools/reopen-row.py per the round-62 closure: redirect targets re-validated against the private-host refusal (a redirect hop to an authority different from the fetching URL's is refused even under --allow-private; at most 5 requests per chain, each counted as an attempt), malformed registry URLs answer `ROW <ID> MALFORMED attempts=0 url=-` with no traceback (exit 1), gzip Content-Encoding decoded, 4 MiB truncation answered TRUNCATED when the quote is absent from the read bytes (LOCATED when inside), and a per-request wall budget via a new `--timeout SECONDS` flag (default 30). Label `ACCEPT-O-63: PASS|FAIL` (legs TOOL INDEP GEN ORDER BOUND EXIT PRIV DEFAULT ERR REDIRECT MALFORMED GZIP TRUNC TIMEOUT REVIEW). Judged ONLY on offline local fixtures; the safety hold lifts only on counter PASS plus the named independent review gate (RevToolA/B/C + residual RevHoldLift, fixed token `VERDICT: NO-OPEN-HIGH-MED`).
- C (coverage, sourced): new entry {LANE}/{ENTRY} (headgear as rank, ritual and identity code - crowns, wreaths, helmets, veils, wraps, caps, hoods) supported by exactly 24 new registry rows S694-S717 (tier A/B, mined, opened 2026-10-23, recheck 180d, used-by the entry, live URL then ` ; capture <web.archive.org id_ URL of the same page>`, anchor quote 8-25 normalised body-text words). Label `ACCEPT-C-63: PASS|FAIL` (legs FILE ROWS ONEID RESTATE LINK APPEND NOHARM SWEEP LIVE; the LIVE leg re-opens the frozen subset S694, S698, S702, S706, S710, S714 with the base locator reports/round-61/reopen-quote.py --row).
The L1 (KotodamaR63) is the sole integration owner and holds the planner seat; it alone writes the lane. Time box: return within 25 minutes of your start; a partial report with what you verified beats none.

# Ownership and bounds (binding)
Every seat is a leaf: no delegation, no background jobs, no swarms (an executor may spawn at most one read-only labrat probe). Every `Report:` trailer path is relative to {LANE} - write it at {LANE}/<that path> with ONE write tool call (absolute path); never edit it afterwards. Seats write NOTHING else in {LANE} and nothing in the fleet repo /home/vgpnk/Projects/shokunin (never a relative path: your tools start at the fleet root). Every other file goes ONLY under {SCR}/<YourName>/ (create it). Never run git or jj write commands in {LANE} or /home/vgpnk/Projects/shokunin; sandbox git only in clones under {SCR}/<YourName>/ made with `git clone -q {LANE} {SCR}/<YourName>/clone && git -C {SCR}/<YourName>/clone checkout -q {REV}`, with GIT_DIR/GIT_WORK_TREE... set for that clone only. Tooling authorization (operator, 2026-10-19): you and every seat may install or upgrade tools that help the task without asking; read /home/vgpnk/.omp/agent/RULES.md first and record each install (tool, version, channel, reason). All pacman transactions are PAUSED host-wide: never pacman -S/-Sy/-Syu/-U/-R, never downgrade, never restart a host service; use uv tool, npx or an official binary in ~/.local/bin, or report the need. Prefer no installs.

# Sources
External reading by ORDINARY MEANS ONLY: plain requests (read tool, curl, python urllib), public copies, archive.org captures. NEVER use a headless browser or anything that gets past a bot challenge, captcha, paywall or login; a challenge met and routed around by a Wayback capture of the same page is fine and is recorded as met-not-passed. Whether a quote locates is decided by `cd {LANE} && timeout 300 python3 -B reports/round-61/reopen-quote.py URL "QUOTE"` (prints LOCATED/NOT LOCATED) or `python3 -B reports/round-61/reopen-quote.py --row S###`. A Wayback capture of a page: query `https://web.archive.org/cdx/search/cdx?url=<url>&output=json&limit=-5&filter=statuscode:200` and use `https://web.archive.org/web/<timestamp>id_/<url>`. Do NOT run tools/reopen-row.py: it is under a safety hold ({LANE}/corpus/QUALITY.md criterion 16).

# Control receipts (Ctl*/Mut* seats)
Score with the frozen counters from YOUR clone at {REV}: `cd {SCR}/<YourName>/clone && timeout 900 python3 -B reports/round-63/accept-o.py; echo exit=$?` (or accept-c.py). Paste every run's FULL stdout and exit code (never tail/head/cut). Never edit a counter except in a clearly labelled PROBE copy under your scratch dir (show its diff). One line per case: `RECEIPT <YourName>/<case> counter-sha256=<sha256 of the counter you ran> rev={REV} frozen=PASS|FAIL exit=<n> stopped-by=<legs that FAIL>`. Then one verdict line per item: `CONTROL-MET` (some cheap fixture that skips the claimed work gets PASS under the frozen counter) or `NONE-MET`, naming the fixture that met it and the smallest counter change that would stop it.

# Row rules (claim C scribes)
A new row has 11 columns mirroring S693 in {LANE}/corpus/SOURCES.md: `| S### | <title>, <publisher>, <date> - <live URL> ; capture <Wayback id_ URL of the same page>. | <kind> | <A|B> | <scope> | <location>, "<verbatim body-text quote>" | <teaches> | mined | 2026-10-23 | 180d | {ENTRY} |`. The quote is verbatim body text (never a caption, never alt/title attributes, never a search-results snippet), 8-25 normalised words, confirmed by the locator on BOTH the live URL and the capture. The entry line you draft is a `- ` bullet ending in ` (S###)`: exactly one S-id, >= 5 content words (>= 4 letters, not stopwords), >= 3 of them in the quote in the quote's order, at most 12 consecutive words copied verbatim. No URL already in {LANE}/corpus/SOURCES.md may be reused (grep it); your URL must differ from every other scribe's (the subtopic list below is the coordination device; if your first choice is taken or fails, move to your second). Never invent or trim a quote to fit; a quote that locates only in a caption is rejected - pick another page.
"""

items = []


def add(name, role, prompt, axes):
    items.append({"name": name, "role": role, "prompt": LEAD + prompt, "axes": list(axes)})


# ---------------- claim O build ----------------
add("ExecRepairTool", "executor",
    f"BUILD item (claim O). Write the repaired tool to {SCR}/ExecRepairTool/reopen-row.py ONLY (the L1 copies it into the lane). Start from the committed source: `git -C {LANE} show {BASE}:tools/reopen-row.py > {SCR}/ExecRepairTool/reopen-row.py`. Implement the full contract in the docstring of {LANE}/reports/round-63/accept-o.py: (1) redirect handling without urllib auto-follow - build the opener with a no-follow handler and follow manually: resolve each Location (urljoin), count every request as an attempt, follow at most 5 requests per chain (a redirect on the 5th response ends the URL as a fatal result), and before requesting a hop whose authority (lowercased host, effective port) differs from the current URL's - or ANY hop when --allow-private is not set - run the same private-host refusal used for listed URLs; a refused redirect ends the URL for the pass; a row with no 2xx answered and every URL pre-refused or redirect-refused prints REFUSED with the requests actually made counted; (2) malformed row URLs (urlsplit ValueError on port/bracketed IPv6, or empty hostname) give the row verdict MALFORMED, attempts=0, no request, no traceback, exit 1; (3) gzip: when the response carries Content-Encoding: gzip, decompress (bounded: gzip.decompress with a cap, e.g. reject expansion beyond 64 MiB) before the charset decode; (4) truncation: read at most MAX_BODY_BYTES+1 bytes; if the quote is found in the read bytes the verdict is LOCATED/CAPTION_ONLY as usual; if not and the body was cut at the cap, verdict TRUNCATED (VERDICT_RANK equal to ABSENT, prints like the other verdicts); (5) --timeout SECONDS (default 30; argparse: a positive number; invalid -> REOPEN_ERROR exit 2) is a per-request wall budget: wrap connect+headers+body read against a monotonic deadline and raise TransientFetch on expiry; (6) keep everything else byte-compatible: all round-62 classes, the schedule, output shape `ROW <ID> <VERDICT> attempts=<n> url=<u>`, summary, exit codes, and extend --selftest with a fixture per new behaviour. Stdlib only, Python 3, module docstring states the contract in your words; the text must not name `reports/`, `accept-o`, `round-63` or `Fixture`. Run your own extended selftest and paste full output. Also run your tool by hand against a local http.server you script in 30 lines: cross-port 302 (REFUSED, target untouched), gzip body (LOCATED), bad-port URL (MALFORMED), and paste outputs.",
    ("operability",))

# ---------------- claim O attack ----------------
CTL = "PRE-DATA CONTROL item (follow the context's control-receipt rules). "
O = "Claim O (accept-o.py). "
add("CtlODoNothing", "mutation-tester", CTL + O + "Do-nothing controls: (a) clone unchanged (the round-62 tool); (b) records-only edits (append a SCORECARD row, LOG line, lesson stub); (c) the tool's docstring edited to claim the repair while the code is untouched; (d) the tool chmod 644. Score each: report which legs pass (TOOL/INDEP pass vacuously: note it) and the smallest change that stops each.",
    ("operability",))
add("CtlOShortCircuit", "mutation-tester", CTL + O + "Short-circuit controls: implement a tool that cheats each new leg minimally: prints TRUNCATED for any 2xx body over 4 MiB without reading it; prints MALFORMED for any URL whose port is non-numeric only; follows cross-authority redirects when --allow-private but answers REFUSED when not (the inverse rule); decompresses gzip only when the body is under 1 MiB; honours --timeout only on the first attempt. Score each: which legs pass, and does GEN catch each cheat?",
    ("operability",))
add("CtlORedirectEdge", "executor", CTL + O + "Redirect-edge fixtures against the frozen counter (build each in your clone's tools/ as an honest attempt, or script the tool under test by hand with local servers): scheme-relative Location `//127.0.0.1:PORT/x`; Location with userinfo `http://u@127.0.0.1:PORT/x`; http->https downgrade to a closed TLS port (transient or fatal?); redirect to a malformed URL (bad port); relative Location without leading slash; 308 with POST-unsafe method (irrelevant for GET: note); chain of exactly 5 then a 200 (attempts=5, LOCATED?); chain where the 5th response is still a redirect (attempts=5, not located). Report which cases the frozen counter pins and any case it leaves unpinned.",
    ("operability",))
add("MutToolNeutral", "mutation-tester", CTL + O + "Neutral-patch kills: take the repaired artifact if present at {SCR}/ExecRepairTool/reopen-row.py (else wait-check once, then use your own minimal implementation of the contract): produce patched copies that each remove ONE defended behaviour - no redirect re-validation; no MALFORMED branch (ValueError propagates); no gzip; no TRUNCATED verdict (silent 4 MiB cap); no per-request deadline (socket timeout only); attempts counted per fetch() call not per request. Score each patched copy with the frozen counter: every patch must turn a PASS into a FAIL (paste the RECEIPT line each). Report any patch that still passes.",
    ("operability",))
REV = ("INDEPENDENT REVIEW GATE item (claim O; the safety hold lifts only if your report ends with the fixed token `VERDICT: NO-OPEN-HIGH-MED`). ")
add("RevToolA", "reviewer", REV + "Review the repaired row-re opener against the SSRF catalog: read {LANE}/tools/reopen-row.py at {BASE} (the held version) and, if it exists when you start, {SCR}/ExecRepairTool/reopen-row.py (the candidate repair). Catalog to check, each with a concrete exploit sketch: cross-host redirect to 127.0.0.1/::1/RFC1918/link-local/0.0.0.0; decimal (http://2130706433/), octal, hex and dotted-less IP literals; userinfo confusion (http://127.0.0.1@public.example/); scheme-relative Locations; https->http downgrade exposing the same path to a private listener; DNS-rebind limitation (honest: the policy is IP-based, note the residual); redirect loops and hop caps; the --allow-private semantics (same-authority hops allowed, cross-authority re-checked). For each item: CLOSED-by (line/function in the artifact you reviewed) or OPEN with severity. Write the report to your Report path; end with the token only if no HIGH or MEDIUM finding is open.",
    ("operability",))
add("RevToolB", "reviewer", REV + "Review the malformed-URL and robustness surface, independent of RevToolA: bad port (99999, -1, empty), unbalanced bracketed IPv6, empty host, whitespace/control chars in the URL, IDNA/punycode hostnames, a URL that is only 'http://', a source cell whose first URL is fine but whose capture URL is malformed (what happens then?), plus interaction of MALFORMED with the pass/retry schedule (does a MALFORMED row stop later passes? it must not retry), and the exit-status contract (registry data error -> exit 1, invocation error -> exit 2). Also the per-request deadline: can a drip body still outlive 3 attempts x budget? can the deadline race the min(gap,5) wait? For each: CLOSED-by or OPEN with severity. End with the fixed token only if no HIGH or MEDIUM is open.",
    ("operability",))
add("RevToolC", "reviewer", REV + "Review the data-integrity surface, independent of RevToolA/B: gzip handling (gzip.decompress cap vs zip-bomb; Content-Encoding case; multiple encodings), the 4 MiB truncation semantics (MAX+1 read; quote split across the cap boundary - is a quote starting before the cap and ending after it TRUNCATED even though its start is present? argue what the contract should say and whether the artifact matches), attempts counting across chains (transient raised mid-chain: are the hops before the failure counted?), the REFUSED-when-redirect-refused verdict against the round-62 verdict vocabulary, and regression risk: every round-62 GEN class must behave byte-identically (the repair must not change BODY/CAP_*/ARCHIVE behaviour). For each: CLOSED-by or OPEN with severity. End with the fixed token only if no HIGH or MEDIUM is open.",
    ("operability",))
add("RevCounterO", "reviewer", CTL + O + "Counter robustness review of {LANE}/reports/round-63/accept-o.py itself: read for false verdicts - the REDIRECT leg's two-server setup (can the tool resolve 127.0.0.1 differently?), the TIMEOUT leg wall bound 45 s on a loaded host, TRUNC pad sizes vs MAX_BODY_BYTES, GEN's REDIRECT_LOOP expecting exactly l1=3/l2=2 (must the tool hit that interleaving?), INDEP's forbidden strings (can an honest tool accidentally contain 'Fixture'?), the REVIEW leg's fixed token (gameable? argue why presence + closure re-read suffices), DEFAULT's 100-600 s window. Report concrete defects with line numbers; mutate in a PROBE copy to demonstrate any false PASS.",
    ("operability",))
add("MutCounterO", "mutation-tester", CTL + O + "Counter mutation: PROBE-copy {LANE}/reports/round-63/accept-o.py under your scratch dir and mutate it - drop the REDIRECT leg; swap TRUNC_FAR to expect ABSENT; weaken TIMEOUT to wall<600; remove REVIEW - then re-score the base tool against each mutated copy. Report which mutations would let the base (unrepaired) tool pass, with RECEIPT lines. This measures whether the counter kills each defended behaviour.",
    ("operability",))

# ---------------- claim C build: 24 row scribes ----------------
TOPICS = {
 "S694": ("pileus / liberty cap (Roman cap of freedom, given to freed slaves; later revolutionary icon)",
          "Britannica pileus; a university classics page on the pileus; Met Museum object page"),
 "S695": ("laurel wreath / corona (Greco-Roman victory and honour crown)",
          "Britannica laurel wreath; Perseus/Pliny on coronae; a museum object page"),
 "S696": ("Roman military crowns: corona civica, corona muralis, corona obsidionalis (awarded valour)",
          "LacusCurtius/Smith dictionary entry; a classics department page; Britannica corona"),
 "S697": ("Phrygian cap (soft conical cap of the East; Mithras; Marianne)",
          "Britannica Phrygian cap; a museum collection page; Smarthistory"),
 "S698": ("crown as regalia (generic: the encircling headpiece of sovereignty and its materials)",
          "Britannica crown regalia; Met Heilbrunn timeline; Royal Collection Trust page"),
 "S699": ("mitre (tall liturgical headdress of bishops; folding or stiff)",
          "Britannica mitre; a cathedral/museum page; Catholic Encyclopedia (newadvent)"),
 "S700": ("turban / dastar (wrapped headcloth; honour, community, status across West and South Asia)",
          "Encyclopaedia Iranica turban entry; Britannica turban; V&A collection page"),
 "S701": ("tagelmust / indigo veil (Tuareg men's headwrap; indigo dyeing)",
          "Smithsonian/NMAfA page; a museum collection; Britannica Tuareg"),
 "S702": ("veil as garment (covering for head/face; modesty, mourning, marriage, sanctuary)",
          "Britannica veil; V&A fashion page; an encyclopedia of clothing entry"),
 "S703": ("flammeum (Roman bridal veil of yellow-orange; the flaminica's veil)",
          "academic article on Roman wedding dress; JSTOR-free classics page; university page"),
 "S704": ("kabuto (Japanese samurai helmet with crests; lacquered plates)",
          "Met Museum kabuto object page; Britannica; a museum collection page"),
 "S705": ("Corinthian helmet (Greek bronze hoplite helmet; evolution to Italic forms)",
          "British Museum collection; Britannica Corinthian helmet; academic page"),
 "S706": ("galea (Roman legionary helmet; types Gallic/Italic/Imperial)",
          "academic page on Roman helmets; a museum object page; Livius.org galea"),
 "S707": ("chaperon / medieval hood (draped hood with liripipe; 14th-15th c. fashion)",
          "V&A medieval fashion page; a museum textile page; Britannica chaperon"),
 "S708": ("gele (Yoruba women's headwrap; structured cloth architecture; occasion and status)",
          "Smithsonian page; Britannica gele; academic page on Yoruba dress"),
 "S709": ("kufi (West African close-fitting cap; prayer and formal dress)",
          "Britannica kufi; a museum collection page; Smithsonian page"),
 "S710": ("tiara / diadem (encircling jewelled band; antiquity to modern pageant)",
          "Britannica tiara; a royal collection page; museum object page"),
 "S711": ("mortarboard / academic cap (square cap of universities; the birretum lineage)",
          "Britannica mortarboard; a university archives page; academic dress society page"),
 "S712": ("wimple and veil (medieval European women's head and neck covering)",
          "V&A page; a museum textile entry; Britannica wimple"),
 "S713": ("cloche hat (1920s close-fitting bell-shaped hat; couture line)",
          "V&A 1920s fashion page; Britannica cloche; a museum collection page"),
 "S714": ("ushanka (fur cap with ear flaps; cold-climate military and civilian)",
          "Britannica ushanka; a museum ethnography page; tier-B dictionary page"),
 "S715": ("sombrero (wide-brimmed hat of Mexico; charro lineage)",
          "Britannica sombrero; a museum collection page; Smithsonian page"),
 "S716": ("bearskin cap (tall fur cap of guards regiments; British/French lineage)",
          "a regimental museum page; Britannica bearskin; Royal Collection page"),
 "S717": ("fez (red felt cap of the Ottoman world; tasselled)",
          "Britannica fez; a museum collection page; Smithsonian page"),
}
for sid, (topic, suggestions) in TOPICS.items():
    subset = sid in ("S694", "S698", "S702", "S706", "S710", "S714")
    add(f"ScribeRow{sid}", "scribe",
        f"BUILD item (claim C, row {sid}). Subtopic: {topic}. Suggested starting points: {suggestions}. " +
        ("THIS ROW IS IN THE FROZEN LIVE SUBSET: pick the most robust tier-A page you can (dictionary/encyclopaedia/museum with a stable URL and several Wayback captures), and re-verify the capture the same hour." if subset else "Tier A or B only.") +
        f" Open ONE page by ordinary means; extract a verbatim body-text quote of 8-25 normalised words about the subtopic; confirm it with `cd {LANE} && timeout 300 python3 -B reports/round-61/reopen-quote.py '<live URL>' '<quote>'`; find a Wayback id_ capture of the same page via CDX and confirm the quote in it too; draft per the context's row rules: (1) the registry row line for {sid} (11 columns, used-by {ENTRY}); (2) the entry bullet line `- <clause> ({sid})` (one S-id, >= 5 content words, >= 3 in quote in order, <= 12 consecutive copied words, no defect marks); (3) a Gate line `## Gate`-ready: `- {sid} | <live URL> | 2026-10-23 | <=25-word quote in double quotes`. Rejections: paste what failed and why (a quote that locates only in a caption/alt/title is rejected; a page that 403s ordinary requests is rejected unless its capture carries the quote - then record met-not-passed). Write all three artifacts plus your locator outputs to your scratch dir AND your Report path; the L1 assembles the entry and registry.",
        ("coverage",))

# ---------------- claim C attack ----------------
add("CtlCJunkRow", "mutation-tester", CTL + "Claim C (accept-c.py). Junk-row controls: in your clone, invent rows that meet ROWS shape but cheat: (a) a real on-topic page with an invented quote that the page does not carry (which leg stops it?); (b) a real page whose quote is on-topic but copied from a DIFFERENT page; (c) a capture URL of a different page than the live URL; (d) a quote from page metadata (description meta); (e) an off-topic page using the word 'crown' (dental crown, chess king, crown ether). Score accept-c.py against each and report which leg stops each, plus the cheapest that passes most legs.",
    ("coverage",))
add("CtlCLineScam", "mutation-tester", CTL + "Claim C. Entry-line controls in your clone: multi-id lines, id-only bullets `- (S694)`, quote-dump lines (the verbatim 25-word quote as the clause), clauses with 4 content words, clauses with 2 in-order words, 13+ consecutive copied words, lines with defect marks like `(to-verify)`, a table row carrying S-ids. Score and report which leg (ONEID/RESTATE) stops each and the cheapest that passes.",
    ("coverage",))
add("CtlCUrlReuse", "mutation-tester", CTL + "Claim C. URL controls in your clone: a new row reusing an existing registry URL (e.g. S693 dictionary.com); a new row whose live URL differs only in query/fragment from an existing one; a new row whose capture embeds a DIFFERENT original URL (same-page check bypass); two new rows sharing one URL. Score and report whether LINK/ROWS stop each.",
    ("coverage",))
add("RevCounterC", "reviewer", CTL + "Claim C. Counter robustness review of {LANE}/reports/round-63/accept-c.py: cells() splitting on `|` inside URLs or quotes; CAPTURE_RE against timestamps with letters (e.g. 2024id_ vs 20240101000000id_) and the rstrip comparison; the RESTATE subsequence check (can a 3-word accidental overlap pass a nonsense clause?); the copy-run window scan's complexity and correctness; APPEND's multiset logic against base rows that legitimately repeat; NOHARM comparing BASE..main (what if the measured tip moves past the claim commit? argue why main is right at receipt time); SWEEP's topic byte-equality against README wrapping; the LIVE leg's locator timeout of 1500 s (enough for 6 rows x 2 URLs x 3 attempts on slow hosts?). Report concrete defects with line numbers; demonstrate any false PASS with a PROBE copy.",
    ("coverage",))
add("MutCounterC", "mutation-tester", CTL + "Claim C. Counter mutation: PROBE-copy accept-c.py and mutate - drop RESTATE's copy-run check; weaken LIVE to 3 of 6 rows; drop LINK; relax ROWS to tier C allowed - then re-score against the base tree. Report which mutations let an empty/no-work tree pass, with RECEIPT lines.",
    ("coverage",))
for sid in [f"S{n}" for n in range(694, 718)]:
    add(f"RevRow{sid}", "reviewer",
        f"BLIND SUPPORT item (claim C, row {sid}). Under {SCR}/ScribeRow{sid}/ (or your own search if that scratch dir is empty when you start: then find an INDEPENDENT page for the same subtopic and say so), re-open the drafted row's live URL by ordinary means (never the held tool), extract the body text, and judge: does the page carry the drafted quote verbatim (8-25 normalised words, body text, not caption/alt/title/meta)? Does the capture URL show the same page with the quote? Does the drafted entry line restate ONLY what the quote carries (no invented claims: dates, peoples, uses beyond the words)? Verdict `SUPPORTED` or `NOT-SUPPORTED` with the pasted located span and reasons. You do not edit the registry or entry; write the verdict to your Report path.",
        ("coverage",))

# ---------------- frontier / records ----------------
add("ScoutEntryOwners", "scout",
    f"RECON item (claim C). In-corpus ownership recon for the headgear entry's `- gap filled:` section: enumerate every corpus/knowledge file that mentions headgear registers (ritual-garments.md, dress-through-eras.md, warrior-material-culture.md, sumptuary-law-rank-display.md, garment-lexicon-crosslinguistic.md, era-myth-language-costume-matrix.md in synthesis) with path:line evidence for each, and state in one line each what it owns that the new entry must NOT restate. Also run the filename/topic sweeps named in claims.json C.unmoved_command and paste outputs. Report only; no edits.",
    ("coverage",))
add("ScoutSiblingO", "scout",
    f"RECON item (claim O + frontier). Sibling-lane recon: read-only scan of sibling repos (never edit) for redirect-handling fetch code and headgear ownership: confirm chousa-shokunin/tools/quote-reopen.py exists and summarize its redirect policy in 5 lines; grep the fleet's sibling repos' tools/ for urlopen/redirect handling and name the strongest prior art; report whether any sibling owns headgear/crown/helmet/veil material culture (one line). Report only.",
    ("operability", "adjacency"))
add("ScribeLesson", "scribe",
    f"RECORDS item (frontier step). Draft corpus/lessons/round-63.md under {SCR}/ScribeLesson/ (the L1 lands it): sections `## Round` (one paragraph: claims O + C, wave shape), `## Mistakes` (skeleton table with candidate rows R63-M1..M5 you can already justify from the round-62 spotcheck routed defects 4-7: the LOG hash-citation gap, the resid filename prefix drift, the 28-vs-32 selftest wording, the S693 kind cell, the unrun separability - for each: class, evidence pointer, captured-by, and the fix this round applies), and `## Gate` (skeleton list for S694-S717, one `- S### | URL | 2026-10-23 | \"quote\"` line each, marked PLACEHOLDER-the-L1-fills-from-scribe-evidence). The L1 finalizes Gate from the scribes' confirmed rows and mistakes from the control receipts.",
    ("calibration",))
add("ScribeCensus", "scribe",
    f"RECORDS item (frontier step). Read {LANE}/corpus/SOURCES.md `## Leads (unopened)` and `## Search log` sections plus CORPUS.md's SOURCES.md contract; propose in your report: (a) any rows whose recheck date forces a re-open in a later round, (b) two to four new candidate leads for the headgear follow-on rounds (names/URLs only, ordinary means check that they resolve, no quotes needed), (c) the exact end-of-round census command and its expected exit. No edits to the registry.",
    ("freshness",))
add("ConnectorOverlap", "connector",
    f"SIBLING-OVERLAP scan (mandatory connector seat). Fleet-wide: which lanes touch material-culture clothing registers (kake web properties, kama serving, kumitate orchestration are negative space - check quickly) and, specifically, whether any lane repo owns or is building headgear/crown/helmet/veil/turban content or a row-reopen/fetch tool this round; name the closest prior art for both claims' surfaces with repo/path evidence. One report, no edits.",
    ("adjacency",))
add("CriticClaims", "critic",
    f"ADVERSARIAL item. Attack both claims at the freeze level: (O) is the frozen predicate 'ACCEPT-O-63: every leg prints PASS' reachable by a do-nothing control (the round-62 tool)? Show the receipt math. Is the REVIEW leg's token check gameable by an empty report carrying the token, and does the kill rule plus closure re-read close that? (C) can a 24-row entry pass RESTATE with lines that say nothing substantive (argue the >= 5 content words + >= 3 in-order rule's weakest gap); is the six-row LIVE subset too small to vouch for 24 rows (state what would make it adequate); is '0 filename owners' true (run the sweeps). Name the single weakest point of each claim in one line each.",
    ("calibration",))

spec = {
    "wave": "kotodama-r63-w1",
    "milestone": "Round 63 single v2 wave (build+attack): reopen-row repair + independent review gate, 24 headgear rows + entry support, controls/counters/recon/records",
    "reportDir": ".ufo/waves/round-63/w1",
    "axes": ["operability", "coverage", "calibration", "adjacency", "freshness"],
    "context": CONTEXT,
    "items": items,
}
path = pathlib.Path(__file__).with_name("w1-spec.json")
path.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
print(f"wrote {path} seats={len(items)}")
from collections import Counter
print(Counter(i['role'] for i in items))
