VERDICT KotodamaR62.ResidLine75: HOLDS

Scope: claim D (depth), line 75 of corpus/knowledge/culture-material/footwear-codes-terminology.md at measured revision a2c5caa59b2d67ce35e53d6ce0217030a66cdd48, and its cited row S666 (corpus/SOURCES.md). Attack question: does line 75 keep the source's hedge ('we have') and its attribution accurately, restating only what the page says, versus base d42ffb89?

## Findings by severity

- NIT (informational, no support impact): the restatement drops the word "from" from the source sentence. Page: "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl." Line 75: "...is a 10th-century Persian bowl." A literalist reading of the page distinguishes evidence *from* a bowl (depiction on it) from the bowl as the evidence; the entry's compression blurs that by one word. It does not change the hedge, the attribution, the date, or the referent, so support holds.
- No HIGH/MEDIUM findings. Line 75 preserves BOTH the hedge ('we have') and the attribution ('According to the BBC article'), and adds nothing the page does not say. Smallest (hypothetical) fix for the nit: "...is from a 10th-century Persian bowl." (not required for the predicate).

## Evidence

### 1. Measured-revision line 75 (a2c5caa), and base line 75 (d42ffb89)

Command (sandbox clone in scratch; no lane writes):
```
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r62/resid/KotodamaR62.ResidLine75/clone
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C <clone> checkout -q a2c5caa59b2d67ce35e53d6ce0217030a66cdd48
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C <clone> rev-parse HEAD   # -> a2c5caa59b2d67ce35e53d6ce0217030a66cdd48
sed -n '63p;74p;75p;93p' <clone>/corpus/knowledge/culture-material/footwear-codes-terminology.md
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C <clone> show d42ffb890a54c8431fa891380b6c38bb608b8362:corpus/knowledge/culture-material/footwear-codes-terminology.md | sed -n '63p;74p;75p;93p'
```

Full output (a2c5caa lines 63/74/75/93):
```
- A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, Belgium, etc. (S692)
- A Bata Shoe Museum image caption says the heel originated in Western Asia centuries ago for horseback riding. (S665)
- According to the BBC article, the earliest evidence we have of someone wearing heels is a 10th-century Persian bowl. (S666)
- Talaria are the wings or winged sandals worn on the feet of Hermes, or Mercury. (S693)
```

Full output (d42ffb89 lines 63/74/75/93):
```
- A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France, and Belgium. (S692)
- A heel originated in Western Asia for horseback riding before Europeans adopted it. (S665)
- The earliest evidence of someone wearing heels comes from a 10th-century Persian bowl. (S666)
- Hermes' talaria were winged leather boots. (S687)
```

Base line 75 = "The earliest evidence of someone wearing heels comes from a 10th-century Persian bowl. (S666)" — NO attribution, NO 'we have' hedge. Measured line 75 restores both.

Diff d42ffb89..a2c5caa confirms only lines 63/74/75/93 changed (4 insertions, 4 deletions, entry file only; full output in evidence trail). Lane working tree matches the measured blob (`cmp` -> WORKTREE-MATCHES-a2c5caa); no installs were made (tooling directive: none needed).

### 2. Live page re-open (ordinary means: curl; no browser)

Command:
```
curl -sSL --max-time 90 -A "Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0" -o <scratch>/www/bbc.html -w "HTTP %{http_code} final=%{url_effective} bytes=%{size_download}\n" "https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes"
```
Full output: `HTTP 200 final=https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes bytes=234982`

### 3. Quote located in body text (grep on saved HTML, lines are file line numbers)

Section-2 heading (bbc.html line 1653):
```
<h2>2. Heeled shoes were originally designed for Medieval soldiers</h2>
```
Body sentence (bbc.html line 1654), exact:
```
<p>The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl. Pictured on this Medieval artefact is a cavalry trooper poised for battle with his heel locked into the stirrup of his horse. That&rsquo;s right, we can thank horses for our heels!</p>
```
Programme attribution (bbc.html line 1564): `<a href="/programmes/p07mdbhg">You're Dead to Me</a>`; JSON-LD Article headline: "You're Dead to Me - Six surprising facts about the history of high heeled shoes", publisher BBC (lines 2695, 2698).

## Judgement

- Exact page sentence: "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl." (section 2, "2. Heeled shoes were originally designed for Medieval soldiers").
- Hedge 'we have': present in line 75, matching the page. PASS.
- Attribution: "According to the BBC article" — accurate (the page is a BBC article under the BBC Radio 4 programme "You're Dead to Me"). PASS.
- Restates only what the page says: the clause "the earliest evidence we have of someone wearing heels is a 10th-century Persian bowl" adds no facts absent from the page (10th century, Persian, bowl, wearing heels all present); the only lexical difference from the quote is the dropped "from" (nit above). Longest verbatim shared run before divergence: "the earliest evidence we have of someone wearing heels is" = 10 words < 12 (COPY-safe).
- Base comparison: at d42ffb89 the hedge and attribution were both absent; the repair restores them. The L1's claimed repair is thus confirmed for line 75.

## Residual risk and verification gaps

- Live page verified today (2026-10-23) at fetch time; page content may drift later. Row S666 also lists a past-dated Wayback capture; capture identity/freshness was not independently re-checked in this seat (out of scope for line-75 sentence fidelity; live page already matches the row's quote verbatim).
- This verdict is a recommendation from a read-only seat; accept-d.py was not run (the L1's first authoritative run is the only receipt and is never re-run to look for a pass).
