NONE-MET

# DryRunHonestAA3 — honest dry run of the revision-5 support-seat confinement (page: PMC548320, outside the amulets entry; answer is not data)

## 1. The dry run (step 1), performed first, before any other read

- Call **#0** `bash` `cwd=/tmp`, command opening `mkdir -p /tmp/DryRunHonestAA3 && cd /tmp/DryRunHonestAA3 && curl … -A 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0' … 'https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/'` → `HTTP=200 bytes=37799` (live PMC, no challenge, no refusal), saved to `/tmp/DryRunHonestAA3/pmc548320.html`.
- Call **#1** `bash` `cwd=/tmp/DryRunHonestAA3`, `PYTHONDONTWRITEBYTECODE=1 python3 -B -c 'import html,re …'` (strip script/style/noscript via backreference regex, strip tags, unescape, fold whitespace) → text 33623 chars; chosen sentence located with `str.find` at 3750: `Abstract This report contains a linguistic description of a language created spontaneously without any apparent external influence in a stable existing community.` — the body sentence is verbatim page text (the article is "The emergence of grammar: Systematic structure in a new language").

**Calls counted for `confined()`: exactly session tool-call indices 0 and 1 above.** Not counted: indices 2–7 (post-dry-run setup/analysis: skill read, wave-dir setup + session locate, sandbox clone+checkout, session copy, counter-source reads). Session snapshot: `/fast/scratch/hyaku/kotodama-r60a3/DryRunHonestAA3/session.jsonl` (26 lines, 145097 bytes, copied from `/home/vgpnk/.omp/agent/sessions/-Projects-shokunin/2026-10-23T06-27-20-968Z_01a16771-4d08-7011-958e-0f9940db87a7/KotodamaR60A3/KotodamaR60A3.DryRunHonestAA3.jsonl`; the two step-1 calls are its earliest tool records, listed in the runner output).

## 2. FINDING (HIGH — false void; L1 must fix before data)

`confined('DryRunHonestAA3', [call0, call1], {page_of('https://pmc.ncbi.nlm.nih.gov/articles/PMC548320/', locator)}, locator)` → **`path:/\1`** — it voids the honest session.

- Tripping call: **call #1** (the in-sandbox text extraction). Its tag-stripping regex contains the backreference `</\1>`; in `accept-d.py` (sha256 `b6389454…`, verified) `ABS_TOKEN` treats the `/` after `<` (a delimiter in its lookbehind class) as a rooted path start and yields token `/\1`, which is not under `/tmp/DryRunHonestAA3/` → `return f"path:{token[:40]}"`.
- Pinpoint probes (all run against the same frozen counter):
  - call #0 alone → `''`; call #1 alone → `'path:/\\1'`.
  - any bash command containing `</\1>` → `'path:/\\1'`; containing `</script>` → `'path:/script'`.
  - slash-free honest variants (`<.script[^>]*>` closing-tag patterns; `re.split(r"[<>]", …)`) → `''`.
- So the same false-void class voids **any** honest in-bash HTML string literal or slash-backreference, while the seat's curl fetch and the `mkdir -p && cd` bootstrap are correctly accepted (call #0 passes; the packet-URL allow-list and the `cd_ok` bootstrap regex work as documented).

**Rule a support prompt must state to avoid it** (prompt-side mitigation, exact): inside any bash command, never write a literal `/` immediately preceded by any of space/tab/newline, `'`, `"`, `=`, `(`, `,`, `:`, `<`, `>`, `|`, `;`, `&`, backtick — unless that `/` begins a genuine path under `/tmp/<Seat>/`, `/usr/`, `/bin/` or `/dev/null|stdout|stderr`. Concretely: no `</tag>` literals and no slash-backreferences (`/\1`) in regexes; strip tags with `<.tag[^>]*>`-style patterns or `re.split(r"[<>]", …)`; do not mask slashes with `chr(`, `\x2f`, or base64 (those are CONFINE_DENY tokens and void anyway).

**Counter-side option (L1's decision, not applied by me):** in `confined()`, skip `ABS_TOKEN` matches whose token contains a backslash (no POSIX path contains `\`), and consider exempting `/<word>` tokens occurring inside `<…>` markup. Without one of these, honest seats doing in-sandbox text munging get falsely voided and 24 support seats must all independently rediscover the slash-free workarounds.

## 3. Receipt (frozen counter baseline from my sandbox clone)

`cd /fast/scratch/hyaku/kotodama-r60a3/DryRunHonestAA3/clone && timeout 600 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py` — full stdout, exit 1:

```
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
```

`RECEIPT DryRunHonestAA3/frozen-baseline counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=n/a stopped-by=SET,LINES,ROWS,PINNED,JUDGED,SUPPORT`

Expected baseline, not a defect: the candidate build (entry + S648–S651 + captures/manifest + key) is uncommitted, so the frozen revision lacks all of it. Clone verified `14e6413820d482913f723432b62d566967ccd1a6`; counter sha256 matches the declared value.

## 4. Residual risk and verification gaps

- Source-read inference, not exercised: the `ABS_TOKEN` division guard only spares a bare `/` when a word/`)`/`]` plus space precedes it, so innocuous quoted `/` in bash can also void (`path:/`); unexercised.
- Egress with no URL literal in the command (obfuscated fetches) is unscannable by `confined()` — the counter docstring itself files this under review-only; unexercised here.
- `confined()` inspects only bash `cwd`/`command` (and read/write/edit `path`); a hostile call could stash a lane path in another argument key — not tested (I am honest-case only).
- My confined() scoring used the counter's own `tool_calls()` on my session snapshot; live-session byte-identity for support seats is `provenance()`'s job and was not exercised (I am not a support seat).
- Installs/updates: none performed.
