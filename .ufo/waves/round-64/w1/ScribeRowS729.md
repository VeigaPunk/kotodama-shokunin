# ScribeRowS729 — local artifact audit

## Behavior and findings

`row.txt` contains the S729 mined row and its worldbuilder bullet. The selected source is Farran, Lee, Yoo, and Oller’s 2016 original peer-reviewed, open-access PLOS ONE research article, “Cross-Cultural Register Differences in Infant-Directed Speech: An Initial Study.” Its primary study compares 19 Lebanese Arabic-speaking mother–infant dyads with 19 American English-speaking dyads. The quoted Results finding reports more infant-directed-speech utterances per minute among the Lebanese mothers across both registers. Tier A applies only to this article’s own empirical comparison; this does not establish a universal rule about Lebanese caregivers.

The direct article page opened successfully. Wayback availability returned a closest capture with status 200 and timestamp `20261002073140`; that archived page also opened and contained the article. The API response had a top-level `url` for the requested original and a nested `timestamp`, but no separate `original` key. The `CAPTURE` line records that returned URL as the original URL. The selected live URL had no existing lane-repository match in either encoded or unencoded query-path spelling.

An initially considered 2025 *Language Development Research* paper on Ku Waru and Nungon was opened, but its PDF, DOI, and candidate landing URL had no Wayback snapshot; the candidate landing request returned HTTP 404. It was not used. No source content was blocked by a bot challenge or paywall.

## Commands, gates, and outcomes

- Created the assigned scratch directory with `mkdir -p /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS729` (no output).
- Web searches used `baby talk infant-directed speech non-Western caregiving society peer reviewed study open access Kaluli` and `baby talk non-Western society caregivers language socialization paper`; results included the PLOS ONE article and the unused PNG article.
- Opened the selected live article and its archived capture with `read`; both exposed the article body and citation. Plain GET command:
  `curl -sL --max-time 60 -o /tmp/S729-plos.html -w 'HTTP %{http_code} %{url_effective}\n' 'https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518'`
  Outcome: `HTTP 200 https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518`.
- Wayback query:
  `curl -s 'https://archive.org/wayback/available?url=https%3A%2F%2Fjournals.plos.org%2Fplosone%2Farticle%3Fid%3D10.1371%2Fjournal.pone.0151518'`
  Outcome: `{"url":"https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518","archived_snapshots":{"closest":{"status":"200","available":true,"url":"http://web.archive.org/web/20261002073140/https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518","timestamp":"20261002073140"}}}`.
- Locator command was run twice from the lane root, including the required final self-check:
  `python3 -B reports/round-61/reopen-quote.py 'https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518' 'with the Lebanese mothers using more IDS Utterances per Minute across both Registers than the American mothers'`
  Both outcomes: `LOCATED https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518`.
- Required mechanical checks: `awk -F'|' 'NR==1 {print "ROW_FIELDS=" NF; print "ROW_CELLS=" NF-2}' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS729/row.txt` returned `ROW_FIELDS=13`, `ROW_CELLS=11`; `printf '%s\n' 'with the Lebanese mothers using more IDS Utterances per Minute across both Registers than the American mothers' | wc -w` returned `17`; `awk 'END {print "ROW_FILE_LINES=" NR}' /home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS729/row.txt` returned `ROW_FILE_LINES=5`.
- Repository URL searches for `journals\.plos\.org/plosone/article\?id=10\.1371%2Fjournal\.pone\.0151518` and `journals\.plos\.org/plosone/article\?id=10\.1371(?:%2F|/)journal\.pone\.0151518` both returned no matches.
- Read the docstring in `reports/round-64/accept-c.py` for the frozen claim-C legs. No acceptance script, test, build, or other gate was run; ACCEPT-C-64 is not claimed as passed.
- The unused PNG candidate was fetched with `curl -sL --max-time 60 -o /tmp/S729-paper.pdf -w 'HTTP %{http_code}\n' 'https://ldr.lps.library.cmu.edu/article/857/galley/653/download/'` (HTTP 200); its Wayback query returned `archived_snapshots: {}`. Wayback checks for `https://ldr.lps.library.cmu.edu/article/view/857` and `https://doi.org/10.34842/ldr2025-857` also returned no snapshots, and the landing request `curl -sL --max-time 60 -o /tmp/S729-landing.html -w 'HTTP %{http_code} %{url_effective}\n' 'https://ldr.lps.library.cmu.edu/article/view/857'` returned HTTP 404.
- Cleanup command `rm -f /tmp/S729-paper.pdf /tmp/S729-landing.html /tmp/S729-plos.html` removed the temporary downloads. These transient files were created outside the assigned scratch directory; they are not retained.

## Touched surfaces and limits

- Wrote `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS729/row.txt` and this requested report.
- No corpus entry, registry row, judge, product code, or lane index was changed. No tool was installed or updated.
- Work was limited to this one row. The acceptance suite’s other corpus, rejection, append-only, and entry checks remain untested; the source’s result is scoped to the study sample and must not be generalized beyond it.

## Artifact paths

- Row artifact: `/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeRowS729/row.txt`
- Scoped report: `.ufo/waves/round-64/w1/ScribeRowS729.md`
