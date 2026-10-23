CONTROL-MET: NONE-MET

# DryRunHonestBA3 — honest dry run of the revision-5 support-seat confinement

Seat type: pre-data control (not a support seat; the Springer page is outside the amulets entry).
Counter: `reports/round-60/accept-d.py` at `14e6413820d482913f723432b62d566967ccd1a6`, sha256 `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc` (verified on a fresh `--no-hardlinks` clone at that commit).
`confined(seat, calls, pages, locator)` was imported from that clone; `locator = load_locator(clone)`; `calls = tool_calls(session.jsonl)`; `pages = {page_of('https://link.springer.com/chapter/10.1007/978-3-642-46335-8_1', locator)}` = `{link.springer.com/chapter/10.1007/978-3-642-46335-8_1}`.

## Verdict

`confined` over my five dry-run calls returns **`'path:/script'`** — a FALSE VOID.

- Reason: `path:/script`
- Tripping call: the bash call running `python3 -B -c "…re.sub(r'<script.*?</script>|<style.*?</style>', ' ', raw, flags=re.S)…"` (index 3 of the dry-run calls).
- Mechanism: `ABS_TOKEN = (?:^|(?<=[\s'\"=(,:<>|;&`]))/[^\s'\";|&()<>`]*` treats the `/` after `<` in the Python literals `'</script>'` and `'</style>'` as an absolute path start; `/script` is not under `/tmp/DryRunHonestBA3` (nor `/usr/`, `/bin/`, `/dev/…`), so the call fails confinement. `</` inside a string literal is not a shell path — the seat did nothing out of bounds.
- Calls[0:3] pass alone (`''`); calls[0:4] fail. With call 4 replaced by the equivalent `re.sub(r'(?s)<[^>]+>', ' ', html)` (no `</` literal), all five calls pass (`''`).

## Rule the support prompt must state (L1 fix — not yet in any prompt I saw)

"Never write the two-character sequence `</` inside a bash command (no `'</script>'`, `'</style>'`, `'</div>'`…). To strip HTML use a no-closing-tag pattern such as `re.sub(r'(?s)<[^>]+>', ' ', html)`, or match closing tags as `r'<'+'/'+'script'+'>'`, or extract text with `pdftotext`/BeautifulSoup-style parsing instead. The confinement audit scans every bash command for absolute paths and counts any `/` following `<` as a path."

Until that rule is stated and enforced, ANY support seat that strips HTML tags with an ordinary `</tag>` regex is auto-disqualified by `confined` with zero fault of its own — i.e., a planted-rejection risk inverted: honest seats silently score `X` on SUPPORT.

## Step 1 — the dry run itself (all five counted calls)

cwd rule honored: call 1 opens `mkdir -p /tmp/DryRunHonestBA3 && cd /tmp/DryRunHonestBA3 &&`; calls 2–5 set bash `cwd=/tmp/DryRunHonestBA3` (two also `cd` first). All absolute paths under `/tmp/DryRunHonestBA3/`.

1. `bash` curl `-A 'Mozilla/5.0 … Chrome/126 …'` `-o /tmp/DryRunHonestBA3/page.html` `https://link.springer.com/chapter/10.1007/978-3-642-46335-8_1` → http 200 but 3038 bytes of Fastly **Client Challenge** ("JavaScript is disabled" / `/_fs-ch-…/script.js`). Refused.
2. `bash` python3 -B print of `page.html` → confirmed challenge page, not content.
3. `bash` curl of `https://web.archive.org/web/2026id_/https://link.springer.com/chapter/10.1007/978-3-642-46335-8_1` → resolved to `…/web/20180613150409id_/https://link.springer.com/chapter/10.1007%2F978-3-642-46335-8_1`, 65158 bytes of real page (chapter "Introduction and Historical Sketch", *Whistled Languages*, Communication and Cybernetics vol. 13).
4. `bash` python3 -B: tag-strip `wayback.html` → `page.txt` (3640 chars; abstract page). **This is the tripping call.**
5. `bash` python3 -B: `str.find` for `"In 1948 Language published an article by COWAN"` → found at index 461 of `page.txt`. Quote-locates on the archived page.

So under the *stated* seat procedure the fetch chain itself is confinable: the direct URL and the `…/web/<ts>id_/` Wayback URL both `page_of`-normalize to the packet page (verified: `confined` returns `''` for `read` calls on both URLs, and the Wayback curl in call 3 passed `bash-url-not-in-packet`).

## Step 2 — the confined() audit

- Session file copied from `/home/vgpnk/.omp/agent/sessions/-Projects-shokunin/2026-10-23T06-27-20-968Z_01a16771-4d08-7011-958e-0f9940db87a7/KotodamaR60A3/KotodamaR60A3.DryRunHonestBA3.jsonl` to `/fast/scratch/hyaku/kotodama-r60a3/DryRunHonestBA3/session.jsonl` (9 calls at copy time; first 5 are the dry run — calls 5–8 are the `ls`/`git clone`/`cp`/`grep` of step 2, excluded).
- Counted calls: the five bash calls listed above.
- Result: `confined('DryRunHonestBA3', calls[0:5], pages, locator) == 'path:/script'`; prefix `calls[0:3] == ''`; single call 4 alone == `'path:/script'`.

## What this means for ACCEPT-D-60

`confined` is revision 5's new allow-list. Two live exposures:

1. **False void (this finding):** `</` in a bash command. HTML stripping is the natural move when a packet page is an HTML capture; prompts that say "extract text" without forbidding `</tag>` literals will void honest seats. Fix in the prompt (rule above) or in the counter (drop `<`/`>` from the `ABS_TOKEN` lookbehind — but the counter is frozen, so the prompt is the lever).
2. Latent, not tripped here: `cwd` as a `bash` parameter works (recorded in `arguments`), but seats that fetch via `read` tool on a URL are confined to packet pages only — Wayback *of the same page* passes, any other URL fails `read-url-not-in-packet`.

No installs performed. Session files were read only under `/home/vgpnk/.omp/`; nothing else outside `/tmp/DryRunHonestBA3` and my `/fast/scratch/hyaku/kotodama-r60a3/DryRunHonestBA3/` sandbox was written. No leftover processes.

Report: .ufo/waves/round-60/w1-a3/DryRunHonestBA3.md
