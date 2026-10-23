VERDICT KotodamaR62.ResidLine63: HOLDS

# Line 63 (S692) residual falsify — SUPPORTED

Scope: footwear entry line 63 at a2c5caa59b2d67ce35e53d6ce0217030a66cdd48 vs cited row S692 in corpus/SOURCES.md; live re-open of the row URL by ordinary means (curl, no browser); comparison with line 63 at d42ffb890a54c8431fa891380b6c38bb608b8362.

## Finding 1 — Line 63 restates only what the page says; open list kept, no added claim, no reversed meaning (SEVERITY: none; no fix needed)

Measured line 63 (git show @ a2c5caa, sed -n '63p'):
    - A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, Belgium, etc. (S692)

Live page fetch (ordinary means, 2026-10-23):
    $ timeout 120 curl -sS -L --max-time 100 -A 'Mozilla/5.0 ... Firefox/132.0' 'https://www.dictionary.com/browse/sabot' -o .../sabot-live.html -w ...
    HTTP 200 downloaded 83147 bytes final-url https://www.dictionary.com/browse/sabot

Exact page sentence (body text, first definition item of the entry — sense 1; also carried verbatim in the page's meta description):
    "a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc."
HTML evidence: <ol class="list-definition"> <li class="item-definition"> <p class="txt-variant-label-short"> a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc. </p> </li>

Comparison:
- Country list: page "Netherlands, France, Belgium, etc." vs line "Netherlands, France, Belgium, etc." — open list kept, same order, same "etc." tail. No closing of the list.
- Claims added: none. "hollowed shoe made from one wooden block" paraphrases "a shoe made of a single block of wood hollowed out"; "worn especially by farmers and workers" is verbatim from the page. No extra fact, region, or qualification.
- Reversed meaning: none. Direction matches (sabot = single-block wooden shoe worn by farmers/workers in NL/FR/BE).

## Finding 2 — Round-61 closed-list defect is repaired at a2c5caa (SEVERITY: none)

Line 63 @ d42ffb890a54c8431fa891380b6c38bb608b8362 (git show):
    - A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, and Belgium. (S692)
Measured line 63 @ a2c5caa (above): "Belgium, etc." — restores the page's open list. The diff between the two revisions touches only the list clause ("France, and Belgium." → "Belgium, etc."); the rest of the line is byte-identical.

## Consistency (read-only, not re-run)

reports/round-62/telemetry/final-measures.txt receipts for line 63: SET PASS differ=[63,74,75,93]; ONEID PASS 63:['S692']; NOMARK PASS; OPEN PASS ids=['S692'] — consistent with the file contents observed here. S692 row itself is unchanged between revs (SOURCES.md diff touches only S687's used-by cell and inserts S693; S692 untouched). The live page matches both the S692 recorded quote and the measured line.

## Residual risk / verification gaps

- The page is a live, mutable web resource; the match is against the page as fetched 2026-10-23. S692 is a base row and lists no Wayback capture; a future page change would not affect the measured revision's fidelity at review time.
- No other senses of sabot on the page contradict the line; the page's second "a shoe made from a single block of wood" item is a separate entry item, not used by the line.
- I did not re-run accept-d.py (the L1 receipt is authoritative); line content was verified directly from the lane and a sandbox clone at both revisions.
- I did not remove the page's semantics; only the first (American, sense 1) definition is the one the line matches.
