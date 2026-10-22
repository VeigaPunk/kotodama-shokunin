# CriticAccessRegex — adversarial inputs for tools/check-source-access.py

Seat: KotodamaR52.CriticAccessRegex (critic, leaf). Date 2026-10-22. Lane HEAD `dea5ece`.
Assigned item: run synthetic SOURCES rows through `tools/check-source-access.py` (read, not
edited), report which bypass phrasings escape, which ordinary routes are flagged, and the
smallest regex change that fixes each one without adding false positives.
Author-lane advice only; this is not an admission ruling.

## Method

- Scratch: `/fast/scratch/hyaku/kotodama-r52/CriticAccessRegex/`. `check-source-access.py` there
  is a byte copy of the lane file (sha256 `e6ff0c44…2fedf`, same hash on both).
- `harness.py` builds one temporary tree per case (`corpus/SOURCES.md` with one 11-cell row
  `S001`, status `mined`, and `corpus/knowledge/p/e.md` citing `(S001)`), then runs
  `python3 -B <script> --root <tree>`. Exit 1 means the row was flagged; exit 0 means it was
  not. 64 cases: 30 bypass, 1 structural, 9 ordinary-route, 24 domain-vocabulary.
- Each candidate regex is spliced into a copy of the script, which is then run on the same
  64 cases, plus `--selftest`, plus a read-only run on the real lane (`--root` set to the
  lane), plus a regex scan over the source/anchor/teaches cells of every `S` row in all 21
  fleet `*/corpus/SOURCES.md` files and every line of `kotodama-shokunin/corpus/knowledge`.
  Run logs: `run1.txt` … `run4.txt`.

## Result 1: every assigned bypass phrasing escapes

Current pattern (`tools/check-source-access.py:32-35`):
`\bheadless\b|\bbypass(?:ed|ing)?\b|\bsolved (?:a |the )?(?:bot )?(?:captcha|challenge)\b`

All of these reach exit 0 with the row `mined` and cited, which is a silent pass
(`run2.txt` ORIGINAL block):

| access note in the source cell | current checker |
|---|---|
| `(opened with Playwright)` | escapes |
| `(fetched via puppeteer)` | escapes |
| `(rendered with Selenium)`, `(Selenium WebDriver session)` | escapes |
| `(solved the Cloudflare check)` | escapes |
| `(used a logged-in session)` | escapes |
| `(cookie from a subscriber account)` | escapes |
| `(through a VPN to get past a geo block)` | escapes |
| `solved the captchas`, `solved a reCAPTCHA`, `solved the hCaptcha`, `after solving the captcha`, `solved the bot-challenge` | escapes (the `solved` branch needs the exact words `solved`, a single space, and a singular `captcha` or `challenge`) |
| `circumvented the paywall`, `paywall by-passed`, `script bypasses the paywall` | escapes (`bypass(?:ed\|ing)?\b` misses `bypasses` and `by-passed`) |
| `passed the Cloudflare Turnstile`, `got past the bot check` | escapes |
| `via undetected-chromedriver`, `fetched through FlareSolverr`, `via institutional EZproxy`, `signed in with a JSTOR account`, `spoofed a browser user agent past the 403` | escapes |
| `headless` written in the **scope** cell (column 5) | escapes: `flagged()` (`:52-53`) joins only source, anchor and teaches |

Caught today: `Headless Chrome render` and `chromium --headless=new` (they contain the bare
word `headless`).

## Result 2: ordinary routes and domain prose that are flagged

The three assigned ordinary routes are **not** flagged: `live page CAPTCHA; read via Wayback`,
`direct page 403; open repository copy`, `AWS WAF challenge; read via Wayback`. The same holds
for `geo-blocked here; read via Wayback capture`, `paywalled; publisher abstract only` and
`login-gated; abstract only`.

The following *are* flagged by the current pattern (exit 1, `mined` row treated as a bypass):

| text | why it is ordinary | where it occurs in real text |
|---|---|---|
| `Cloudflare challenge, not bypassed; read via Wayback` | the access note denies a bypass | synthetic |
| `no headless browser used; read via Wayback` | the access note denies a bypass | synthetic |
| `supersedes S094 — S094 was opened via headless browser; this scan is the ordinary copy` | a flip row that tells another row's history | synthetic; this is the flip route S132 promises (`corpus/SOURCES.md:161`) |
| `headless burial` | archaeology | `corpus/knowledge/civilizations/nazca.md:119` |
| `headless dbu med` | Tibetan script style | `corpus/knowledge/civilizations/tibet.md:52` |
| `the "ideograms bypass sound" reading` (DeFrancis 1989) | a claim about writing | `corpus/knowledge/linguistics/writing-systems.md:26` |
| `outsider's bypass`, `bypassed` | ordinary prose | `dine-navajo.md:95`, `loanword-material-dating.md:50`, `worldbible-integration-contract.md:19`, `costume-era-consistency-gate.md:142`, `provenance-audit-ledger-format.md:104` (all under `corpus/knowledge/`) |
| `headless relative clauses`, `headless (exocentric) compounds` | syntax and morphology terms | synthetic; plausible for a linguistics lane |
| `Ventris solved the challenge of Linear B` | decipherment history | synthetic |

The checker reads only SOURCES cells, so these knowledge lines are not findings today. They
show that the lane's own prose uses these words in ordinary senses, so a `teaches` cell
summarizing DeFrancis, Tibetan scripts or Nazca burials would trip the checker. Across the
fleet the current pattern also matches 10 non-kotodama SOURCES rows: Godot `--headless` in
audio, game-dev-2d, game-dev-3d and kumitate, and security-sense `bypass` in kaidoku S016,
mado S099 and tabi S077. That only matters if the checker is reused outside kotodama.

## Smallest fix A: additive, adds no false positives (recommended for this round)

Keep the three existing alternatives exactly as they are and add one alternative per escape
family. Drop-in, tested exactly in this form (`additive3.re`, sha256 `9656278f…74d3`):

```python
BYPASS = re.compile(
    r"""\bheadless\b|\bbypass(?:ed|ing)?\b|\bsolved\ (?:a\ |the\ )?(?:bot\ )?(?:captcha|challenge)\b
| \b(?:undetected-chromedriver|flaresolverr|cloudscraper|curl-impersonate|ez-?proxy)\b
| \b(?:open|fetch|load|render|retriev|scrap|access|download|captur|driv|automat)\w*\s+(?:\S+\s+){0,2}?(?:with|via|through|using|by|in)\s+(?:a\s+|an\s+|the\s+)?(?:playwright|puppeteer|selenium|webdriver|chromedriver)\b
| \b(?:playwright|puppeteer|selenium)(?:[\s-]+webdriver)?[\s-]+(?:browser|session|script|chrom\w*|firefox|webkit)\b
| (?<!\bnot\ )(?<!\bno\ )(?<!\bnever\ )\b(?:bypass(?:ed|es|ing)?|by-pass(?:ed|es|ing)?|circumvent(?:ed|s|ing)?|evad(?:ed|es|ing)|defeat(?:ed|s|ing)?|solv(?:ed|es|ing)|pass(?:ed|es|ing)?|clear(?:ed|s|ing)?|g[eo]t(?:ting)?\s+(?:past|around|round|through))\s+(?:\S+\s+){0,3}?(?:pay-?walls?|log-?ins?|sign-?ins?|(?:re|h)?captchas?|turnstile|geo[\s-]?block(?:s|ed|ing)?|geo[\s-]?fenc(?:e|es|ing)|(?:bot|js|javascript|cloudflare|waf|anti-?bot|browser|security)[\s-](?:challenges?|checks?|blocks?|walls?|tests?)|challenge\s+pages?|access[\s-]controls?)\b
| \b(?:pay-?wall|log-?in|(?:re|h)?captcha|geo[\s-]?block)s?\s+(?:was\s+|were\s+)?(?:bypass|by-pass|circumvent|evad|defeat|solv)\w*
| \bvpns?\b
| \blogged-in\b|\b(?:signed|logged)\s+in\s+(?:as|with|via|using|through)\b
| \b(?:subscriber|subscription|paid|member)\s+(?:account|login|credentials|session|cookie)s?\b|\b(?:institutional|personal)\s+(?:login|credentials|session|cookie)s?\b|\bsession\s+cookies?\b|\bcookies?\s+(?:from|of)\s+(?:a|an|my|the)\b
| \bspoof(?:ed|ing|s)?\s+(?:a\s+|an\s+|the\s+)?(?:browser\s+)?(?:user[\s-]agent|ip|location|referr?er|headers?)\b""",
    re.IGNORECASE | re.VERBOSE,
)
```

Which alternative fixes which escape, and why each one is anchored to context:

| escape | alternative | why not the bare word (measured) |
|---|---|---|
| Playwright, puppeteer, Selenium | access verb + `with/via/through/using/by/in` + tool name; or tool name + `browser/session/script/chrome/firefox/webkit` | `playwright` is a theatre noun, `puppeteer` a puppetry noun, `selenium` an element. Bare tool names match 23 lines of tabi's SOURCES; bare `webdriver` matched 10 tabi rows (W3C WebDriver BiDi spec, Selenium docs; additive v1 in `run1.txt`). The anchored form matches none. |
| Cloudflare check, captcha variants, Turnstile, bot check, circumvent, `bypasses`, `by-passed` | verb (`bypass/circumvent/evade/defeat/solve/pass/clear/get past|around|through`) followed within 3 words by an access-control noun; or the noun followed by the verb | The noun list leaves out bare `challenge`, `gate`, `check` and `bot` (with no qualifier after it), so `the hero must get past the gate guardian` and `passed the bottle gourd` stay clean. A `not/no/never` lookbehind keeps `not bypassed` clean on this branch. |
| logged-in session | `logged-in`; `signed/logged in` + `as/with/via/using/through` | Bare `logged in` is the lane's ledger idiom: `corpus/knowledge/synthesis/migration-founder-effects.md:202` ("decisions are logged in `../../lessons/…`"), `corpus/lessons/round-51-verifier-spotcheck.md:63`. |
| cookie from a subscriber account | `subscriber/subscription/paid/member` + `account/login/credentials/session/cookie`; `institutional/personal` + `login/credentials/session/cookie`; `session cookie`; `cookie from/of a` | `institutional account` is narrative prose in 5 kotodama entries (`ancestral-puebloan.md:108`, `germanic-norse.md:118`, `hawaii.md:107`, `mesopotamia-sumer-akkad.md:191`, `siam-thai.md:23`), all matched by additive v1 (`run1.txt`), so `account` is not allowed after `institutional/personal`. |
| VPN to get past a geo block | `\bvpns?\b`, plus the verb + `geo block` branch | 0 occurrences in any fleet SOURCES row. Bare `proxy` and `tor` are left out because of `person-proxy` (`dress-through-eras.md:73`) and place names like `Glastonbury Tor`. |
| chromedriver, FlareSolverr, EZproxy, UA spoofing | named bypass tools by themselves; `spoof` + `user agent/ip/location/referrer/headers` | `spoof` alone means parody. |

Measured result for fix A (`run3.txt`, VARIANT additive3):
- All 30 bypass cases are flagged. 23 of them escape the current pattern; the other 7 already
  contain a bare `headless`, `bypass` or `solved the challenge`.
- The current selftest still passes 10/10. The real lane is unchanged: exit 0, `2 flagged rows`
  (S094, S132), `0 findings`.
- It matches the same 12 fleet SOURCES rows and the same 8 kotodama knowledge lines as the
  current pattern, so it adds no false positives on real text.
- It removes none of the existing false positives (12 case mismatches remain: the ordinary and
  domain rows in Result 2, plus the scope-cell escape).

## Fix B: also narrow the three existing alternatives (removes existing false positives, at a cost)

Replace the first line of fix A with:

```
(?<!\bno\ )\bheadless[\s-]+(?:browser|chrom\w*|firefox|webkit|mode|shell)\b|--headless\b|\b(?:opened|fetched|loaded|rendered|scraped|read|ran|run)\s+headless(?:ly)?\b
```

This drops bare `bypass` and the old `solved … challenge` branch; the verb + access-control
branch already covers both. Measured (`run3.txt`, VARIANT narrow3):
- 4 of 64 cases mismatch instead of 12. It fixes `not bypassed`, `no headless browser`,
  `headless relative`, `headless (exocentric) compounds`, `headless burial`,
  `headless dbu med`, `ideograms bypass sound`, `bypassed the spoken channel`, the
  `ring-road bypass` and `Ventris solved the challenge`.
- Kotodama knowledge lines matched: 8 → 0. Fleet SOURCES rows matched: 12 → 6. The 6 left are
  S094, S132 and Godot `--headless`.
- Lane run unchanged (2 flagged, 0 findings); selftest 10/10.
- **Cost: two new escapes.** A note that just says `(headless)` and one that says
  `(opened by bypass)` with no access-control noun are no longer flagged, and
  `solved the challenge` with no qualifier (other than `challenge page`) is no longer flagged.
  This is a real tradeoff for the integrator to accept or reject; it is not a pure improvement.
- **Required companion edit if B is taken:** the selftest control `prefix-id-not-cited`
  (`tools/check-source-access.py:115`) uses the row `(headless)`. Under B that row is not
  flagged, so the cited-leg prefix test (`S0011`, `S00`) runs with an empty id set and passes
  without testing anything. Change its source note to `(opened via headless browser)`.

## Structural escape (not a regex fix)

A bypass note in the `scope` cell is never read. The smallest fix is to add `"scope": cells[4]`
in `parse_rows` (`:47-48`) and include `r["scope"]` in the join in `flagged` (`:53`). Tested
together with fix B (`run4.txt`, VARIANT narrow3+scope): the scope-cell case is flagged, the
lane run and selftest are unchanged, and no kotodama scope cell matches. The only fleet
scope-cell matches are Godot `headless` (game-dev-2d :12, game-dev-3d :12 and :43) and a
`permission-bypass` scope in tsukuroi :33.

## Residuals that no regex fixes

- **Flip-row narration.** A later `mined` row that supersedes S132 with an ordinary copy and
  re-tells S094's history (`… S094 was opened via headless browser …`) is flagged under both
  fixes, because the history-telling row is supposed to be S132 itself, which is `rejected`.
  The smallest correction is a convention, not a regex: the flip row's `teaches` says
  `supersedes S132 — <ordinary route>` and points to S132 for the reason instead of restating
  the method.
- **Silence escapes everything.** The checker can only catch a bypass that the row itself
  reports. A row opened through a bot challenge whose source cell gives only the URL passes
  under every variant. S094 was caught only because its author disclosed the headless browser
  (`corpus/SOURCES.md:123`). Criterion 10 still depends on honest access notes and the lesson's
  `## Gate` record; the checker is a tripwire for self-reported bypasses, not proof of ordinary
  access.
- The case set was written by this seat. A clean run on it shows that these phrasings are
  handled, not that the vocabulary is complete.

## Selftest additions worth landing with either fix

Rows to add to the selftest (and update the hard-coded `10/10` total at `:138`):
`(opened with Playwright)` with status `mined` gives exit 1; `(cookie from a subscriber account)`
with `mined` gives exit 1; `(through a VPN to get past a geo block)` with `mined` gives exit 1;
the `teaches` text `a household story, an institutional account` with `mined` gives exit 0;
`W3C WebDriver BiDi` as the source title with `mined` gives exit 0. If fix B is taken, also add
`headless dbu med traditions` (exit 0) and `Cloudflare challenge, not bypassed; read via
Wayback` (exit 0).

## Checks run, checks not run, installs

- Run: the harness on the original and six variants; `--selftest` for each; a read-only lane
  run for each; fleet-wide regex scans. No lane file was edited apart from this report. No jj or
  mutating git command was used.
- Not run: the lane's full gate suite under a patched checker. That is for the L1 after
  integration: `python3 -B tools/check-source-access.py`, the same with `--selftest`, plus the
  lane's usual corpus gates.
- Installs: none.
