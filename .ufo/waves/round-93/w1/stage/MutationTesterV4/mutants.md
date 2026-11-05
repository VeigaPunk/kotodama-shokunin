# MutationTesterV4 — round-93 v4 gap hunt (ten NEW single-line mutants)

Target: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-advance-evidence.py`
sha256 `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7` (verified 2026-11-05; unchanged after the run).
Detector: each mutant's own `--selftest --work <scratch subdir>`; KILLED iff exit non-zero.
Baseline: pristine bytes, rc 0, `SELFTEST PASS 114/114` — detector valid; all verdicts conclusive.
Every mutant below is absent from `reports/round-93/mutants.py` (all 77 pairs checked by name and target string).
Raw outputs: `mutants-raw.json` (same stage dir). Mutants lived in `/fast/scratch/hyaku/kotodama-r93/MutationTesterV4/` (deleted on exit).

## Result rows

| # | tag | target line (tool) | change | rc | SELFTEST line | verdict |
|---|-----|--------------------|--------|----|---------------|---------|
| 1 | script-strip-off | L291 `s = re.sub(r'(?is)<(script\|style)\b[^>]*>.*?</\1\s*>', ' ', s)` | sub removed (`pass`) | 0 | `SELFTEST PASS 114/114` | SURVIVED |
| 2 | comment-strip-off | L292 `s = re.sub(r'(?s)<!--.*?-->', ' ', s)` | sub removed (`pass`) | 0 | `SELFTEST PASS 114/114` | SURVIVED |
| 3 | unescape-off | L294 `return _html.unescape(s)` | `return s` | 0 | `SELFTEST PASS 114/114` | SURVIVED |
| 4 | dispo-any-casei | L113 `DISPO_ANY_RE = re.compile(r'\bS(\d{3,})\b.*?\b(NOT[ _-]?LOCATED\|LOCATED)\b')` | `, re.I` appended | 0 | `SELFTEST PASS 114/114` | SURVIVED |
| 5 | baserows-drop-cell8 | L676 `for i in (0, 1, 2, 3, 4, 5, 6, 8):` | `(0, 1, 2, 3, 4, 5, 6)` (cell 8 `opened` dropped) | 0 | `SELFTEST PASS 114/114` | SURVIVED |
| 6 | head-floor-3 | L576 `return len(h.lstrip('#').split()) >= 2` | `>= 3` | 1 | `SELFTEST FAIL 90/114` (BAD `positive entry` … `failed=TOPIC`) | KILLED |
| 7 | gate-extra-slice-2 | L736 `for extra_line, extra_q in gates.get(rid, [])[1:]:` | `[2:]` | 1 | `SELFTEST FAIL 113/114` (BAD `entry mode: second chrome quote on a gate line refused: rc=0 … PASS legs=9/9`) | KILLED |
| 8 | gradednorm-key-sha | L524 `graded_norms[norm(raw.decode('utf-8', errors='replace'))] = g` | key → `hashlib.sha256(raw).hexdigest()` | 1 | `SELFTEST FAIL 113/114` (BAD `entry mode: newline-padded entry copy capture refused: rc=0 … PASS legs=9/9`) | KILLED |
| 9 | archive-year-le | L357 `if int(stamp[:4]) < int(as_of[:4]):` | `<` → `<=` | 1 | `SELFTEST FAIL 113/114` (BAD `same-year archive accepted: rc=1 … FAIL legs=6/7 failed=ARCHIVE`) | KILLED |
| 10 | manifest-msg-reword | L507 `raise Refused('manifest rows is not a JSON object (list where mapping expected)')` | message → `'manifest rows is not a mapping (…)'` | 1 | `SELFTEST FAIL 113/114` (BAD `…_ERROR: manifest rows is not a mapping (list where mapping expected)`) | KILLED |

Counts: **5 KILLED, 5 SURVIVED, 0 inconclusive** (baseline green first).

## Survivor analysis (coverage findings; no contract change proposed)

### 1. script-strip-off — script/style stripping in `html_body_text` unpinned
The only markup-only capture fixture (`entry mode: markup-only capture refused`, A6e) hides its quote in a
`<meta name="description" content="…">` attribute, which the generic tag-stripper `<(?s)<[^>]+>` already removes.
No fixture places a quote inside `<script>`/`<style>`. Behaviour let through: a capture whose only occurrence of
the manifest quote sits inside a `<script>` (e.g. JSON-LD) or `<style>` block still counts the quote as located
body text, because generic tag stripping leaves script/style *content* in the text. Counterfeit-exploitable: yes —
a page with paywalled/empty body and the quote only in `<script type="application/ld+json">` passes CAPTURE.

### 2. comment-strip-off — HTML comment stripping unpinned
No fixture carries a quote inside `<!-- … -->`. Behaviour let through: a quote that exists only in an HTML
comment survives tag stripping (comments' inner text is kept) and counts as located body text.
Counterfeit-exploitable: yes — the cheapest counterfeit of all (`<!-- the quote -->` on an otherwise empty page).

### 3. unescape-off — entity unescape unpinned
No fixture contains HTML entities. Behaviour change is the strict direction: a capture whose body entity-encodes
characters (`&amp;`, `&quot;`, `&#39;`) no longer matches a manifest quote carrying literal characters — a false
refusal of legitimate evidence rather than a counterfeit channel. Coverage finding: the decode step is unpinned
in both directions.

### 4. dispo-any-casei — case-sensitivity of the unanchored disposition scanner unpinned
Lines 111-112 document that lowercase prose ("S001 located in the archive") carries no uppercase verdict token and
stays clean, but no fixture exercises it. Behaviour let through by pristine bytes: a lowercase verdict token in an
unanchored line (table row, bold-wrapped, mid-prose) is invisible to `dispositions()`. Counterfeit-exploitable: yes —
an evasion channel: a disposition flip on an old id written lowercase and unanchored (`s002 not located …`) is never
read, so APPENDONLY stays green while the record quietly flips. The mutant (case-insensitive scanning) would refuse
it; its survival shows neither reading is pinned.

### 5. baserows-drop-cell8 — `opened` identity cell movement unpinned
A6a fixtures pin `teaches` (cell 6) movement; no fixture moves `opened` (cell 8) between base and lands. OTHERCELLS
guards only population rows (recheck-only), so for a base row outside the population a rewrite of `opened` leaves
BASEROWS green. Behaviour let through: provenance backdating/forward-dating of a base row's `opened` date.
Counterfeit-exploitable: yes — a lands registry that rewrites an existing base row's `opened` (e.g. to make an old
row look newly mined, or to align with a fabricated newids/opened story) is not refused by any leg.

## Killed mutants (pinned from the kill side)
- head-floor-3: a positive fixture anchors a phrase through a 2-token heading, so the `>= 2` floor is pinned by use
  (with single-token refusal pinned by A4a, the floor is pinned from both sides).
- gate-extra-slice-2: the A6f fixture (second chrome quote) goes green under `[2:]` — extra-quote loop is pinned.
- gradednorm-key-sha: the A3b newline-padded entry-copy fixture goes green — the normalized-text key is load-bearing
  (build-side mutation is caught even though the lookup side is separately pinned by capture-textcopy-off).
- archive-year-le: `same-year archive accepted` fails ARCHIVE under `<=` — the same-year acceptance is pinned.
- manifest-msg-reword: rc 2 is kept but the diagnostic text is pinned by substring — the refusal message path is
  content-pinned, not just rc-pinned.

## Evidence hygiene
- Commands: `sha256sum <tool>` (before), `python3 driver.py` (one process: baseline selftest + 10 mutant selftests,
  each `python3 <copy> --selftest --work <scratch/work-<tag>>`), `sha256sum <tool>` (after). Driver rc 0.
- Restoration evidence: lane tool bytes never written; sha256 before = after = `9799a96c…aae7`; all mutant copies and
  work dirs lived under `/fast/scratch/hyaku/kotodama-r93/MutationTesterV4/` and were removed on exit (dir absent, rc 2).
- No pacman, no sysctl, no network, no lane writes outside the two named stage files (`mutants.md`, `mutants-raw.json`)
  plus the report trailer.
