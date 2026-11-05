# ScoutReopen — round-93 independent re-open of the four admitted rows and the two unreachable candidates

Seat: ScoutReopen (leaf member, no dispatch). Lane: `kotodama-shokunin`.
Stage: `.ufo/waves/round-93/w1/stage/ScoutReopen/reopen.md`
Scratch (deleted on exit): `/fast/scratch/hyaku/kotodama-r93/ScoutReopen/`
Date of all measurements: 2026-11-05.

Method: ordinary HTTPS only. `curl -sS -L -A "<default browser UA>" --max-time 60 <url>`,
no `-k`, no headless browser, no login, no challenge bypass. Bodies written to scratch
only; not copied into the stage dir. Quote location test: NFKC, curly apostrophes -> `'`,
tags stripped, whitespace collapsed, case-folded; plus a second verbatim raw-HTML
substring test. Capture comparison against
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-93/evidence/S96*.html`.

## Table

| id | url | http status | fetch instant (offset) | quote located | sha256 equal to capture |
|----|-----|-------------|------------------------|---------------|-------------------------|
| S961 | https://bop.unibe.ch/linguistik-online/article/view/1426 | 200 | 2026-11-05T12:44:22,162689479-03:00 | yes | yes — 61f464e407b3245e6f3db7b7efa6ba7a658080e0832ff851efdc07e661214af1 |
| S962 | https://pressto.amu.edu.pl/index.php/srp/article/view/21548 | 200 | 2026-11-05T12:44:22,162671139-03:00 | yes | no — fresh e68db9c6d11f33ad826c00e4c876d0ab940eeb4409788ed11cd02a6de9dc3fa3 vs capture 098eed5cda92aa440dd645d223970b2457d7d7748d6c6fa35bccea80a5b8fbdc |
| S963 | https://bop.unibe.ch/linguistik-online/article/view/3847 | 200 | 2026-11-05T12:44:22,162800229-03:00 | yes | yes — 3eb97d8a59c7af45cbcf64c2ec234b674233921c5957f8bad8d4ed4d66d57a9c |
| S964 | https://oaj.fupress.net/index.php/ss/article/view/17732 | 200 | 2026-11-05T12:44:22,162742279-03:00 | yes | yes — c8eba504c3c049d281e49d5fd1b267295bb578c84c379e48e8bf6b77140188ed |
| MDPI (candidate) | https://www.mdpi.com/2226-471X/11/9/179 | 403 | 2026-11-05T12:44:22,162733869-03:00 | n/a | n/a — Akamai "Access Denied" body, 398 B |
| BEJAIA (candidate) | https://univ-bejaia.dz/revue/jslcs/article/view/394 | 000 (no HTTP response) | 2026-11-05T12:44:22,162661969-03:00 | n/a | n/a — TLS verify failure, curl rc 60 |

## Verdict per row

| id | verdict | reason |
|----|---------|--------|
| S961 | AGREE | Fresh open 200. Quote located verbatim in the fresh body and in the capture. Fresh sha256 equals capture sha256 byte-for-byte. |
| S962 | AGREE | Fresh open 200. Quote located verbatim in the fresh body and in the capture. sha256 differs from capture by exactly one line — the session `csrfToken` hidden input (`fb2501f7a93b4858b3b289b634904211` -> `58759ad460c7dd57ab4024ce98ec1f26`); normalized text of the two bodies is identical (9727 chars, `equal_text True`). Dynamic nonce, not a content change; capture is intact (capture sha256 == manifest sha256). |
| S963 | AGREE | Fresh open 200. Quote located verbatim in the fresh body and in the capture. Fresh sha256 equals capture sha256 byte-for-byte. |
| S964 | AGREE | Fresh open 200. Quote located verbatim in the fresh body and in the capture. Fresh sha256 equals capture sha256 byte-for-byte. |
| MDPI | UNREACHABLE (consistent with the lane record) | HTTP 403, Akamai Access Denied page. Body matches the shape of `reports/round-93/evidence/unreachable-mdpi-403.raw`; only the Akamai error reference differs (`...1793893462.7dcd936b` vs captured `...1793891533.7d487a28`). No bypass attempted. |
| BEJAIA | UNREACHABLE | No HTTP response. `curl` rc 60, `unable to get local issuer certificate (20)`. Confirmed independently with `openssl s_client` (verification ON): `verify error:num=21:unable to verify the first certificate`, `subject=CN=*.univ-bejaia.dz`, `issuer=C=US, O=Let's Encrypt, CN=YR1`, `Verify return code: 21` — the server omits the intermediate. No `-k`, no TLS bypass. |

## Located context spans (fresh opens, exact substrings of the fetched bodies)

- S961: `...one type of politeness in particular, namely the speech acts of greeting and leave-taking denoted by the German verb grüssen.`
- S962: `...greeting formulas derivated from the atelic predicate besar las manos (y los pies) 'to kiss the hands (and feet)', which, despite their apparent formal resemblance, came to codify totally opposite socio-pragmatic values.`
- S963: `...due to pervasive contact between Ngoni and Swahili, greetings tend to be brief today and there is a widespread use of code-switching by all age groups.`
- S964: `...elicited situationally bound responses and compiled a pool of words, expressions, and sayings that speakers reported using when saying goodbye to both acquaintances and strangers.`

Each of the four quotes is also a verbatim substring of the corresponding capture file
(`S961.html`..`S964.html`), confirmed without tag stripping.

## Commands run

| command | rc |
|---------|----|
| `curl -sS -L -A "<UA>" --max-time 60 <S961 url> -o S961.body -w '%{http_code}'` | 0 (status 200) |
| `curl -sS -L -A "<UA>" --max-time 60 <S962 url> -o S962.body -w '%{http_code}'` | 0 (status 200) |
| `curl -sS -L -A "<UA>" --max-time 60 <S963 url> -o S963.body -w '%{http_code}'` | 0 (status 200) |
| `curl -sS -L -A "<UA>" --max-time 60 <S964 url> -o S964.body -w '%{http_code}'` | 0 (status 200) |
| `curl -sS -L -A "<UA>" --max-time 60 <MDPI url> -o MDPI.body -w '%{http_code}'` | 0 (status 403) |
| `curl -sS -L -A "<UA>" --max-time 60 <BEJAIA url> -o BEJAIA.body -w '%{http_code}'` | 60 (TLS verify failure, no HTTP response) |
| second independent fetch of the four admitted rows (round 2) | 0 each (200 each); S962 sha again differs (d443b9d5ce07c2dac32271a7e823ed24b6c33d18b4f671a4bf456bc0448cca4e), other three sha unchanged |
| `openssl s_client -connect univ-bejaia.dz:443 -servername univ-bejaia.dz` (verification ON) | chain incomplete, verify code 21 |
| `sha256sum` of fresh bodies vs capture files; Python normalized-text diff (S962) | fresh/cap sha as tabulated; S962 `equal_text True` |
| `diff <fresh MDPI body> reports/round-93/evidence/unreachable-mdpi-403.raw` | 1 (Akamai error reference line only) |

## Numbers measured

- 4/4 admitted rows re-opened with HTTP 200 and their exact quote located in the fresh body.
- 4/4 quotes also verbatim substrings of the capture files.
- 3/4 fresh bodies byte-identical to the capture (sha256 equal); 1/4 differs only by a
  per-session CSRF nonce (normalized text identical).
- 2/2 unreachable candidates re-checked once each and still unreachable
  (MDPI 403; BEJAIA TLS verify rc 60 / openssl verify code 21).
- Manifest sha256 for all four rows matches the capture file on disk (4/4).

## Tooling

No installs or upgrades were needed. Tools used, all pre-existing:
`curl 8.23.0 (x86_64-pc-linux-gnu) libcurl/8.23.0 OpenSSL/3.6.5`,
`openssl 3.6.5`, `python3 3.14.8`. No pacman transaction was run (host-wide pacman pause
observed). No sysctl was touched. No git/jj mutation was run; no writes outside the seat
stage dir, this report file, and the seat scratch dir (scratch removed on exit).

## Not measured / limits

- The BEJAIA candidate could not be reached at all, so no quote could be tested for it.
- The MDPI candidate returned a bot-challenge page rather than an article; no quote could
  be tested for it.
- Whether the two unreachable candidates would ever serve the article under a different
  but still ordinary client is out of scope: both are recorded UNREACHABLE for this purpose.
