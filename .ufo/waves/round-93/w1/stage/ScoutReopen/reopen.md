# Round-93 independent re-open of the admitted rows and the unreachable candidates

Seat: ScoutReopen. Date: 2026-11-05. Lane: kotodama-shokunin.
Method: ordinary HTTPS only — `curl -sS -L` with a default browser user agent, no `-k`,
no browser, no login, no challenge bypass. Bodies saved to the seat scratch dir only
(`/fast/scratch/hyaku/kotodama-r93/ScoutReopen/`); not copied into the stage dir.
Text normalization for quote location: NFKC, curly apostrophes -> `'`, tags stripped,
whitespace collapsed, case-folded. Quote check also run on the raw HTML without tag
stripping (verbatim substring test) — all four pass both ways.

| id | url | http status | fetch instant (offset) | quote located | sha256 equal to capture |
|----|-----|-------------|------------------------|---------------|-------------------------|
| S961 | https://bop.unibe.ch/linguistik-online/article/view/1426 | 200 | 2026-11-05T12:44:22,162689479-03:00 | yes | yes (61f464e407b3245e6f3db7b7efa6ba7a658080e0832ff851efdc07e661214af1) |
| S962 | https://pressto.amu.edu.pl/index.php/srp/article/view/21548 | 200 | 2026-11-05T12:44:22,162671139-03:00 | yes | no (e68db9c6d11f33ad826c00e4c876d0ab940eeb4409788ed11cd02a6de9dc3fa3 vs capture 098eed5cda92aa440dd645d223970b2457d7d7748d6c6fa35bccea80a5b8fbdc) |
| S963 | https://bop.unibe.ch/linguistik-online/article/view/3847 | 200 | 2026-11-05T12:44:22,162800229-03:00 | yes | yes (3eb97d8a59c7af45cbcf64c2ec234b674233921c5957f8bad8d4ed4d66d57a9c) |
| S964 | https://oaj.fupress.net/index.php/ss/article/view/17732 | 200 | 2026-11-05T12:44:22,162742279-03:00 | yes | yes (c8eba504c3c049d281e49d5fd1b267295bb578c84c379e48e8bf6b77140188ed) |
| MDPI (candidate) | https://www.mdpi.com/2226-471X/11/9/179 | 403 | 2026-11-05T12:44:22,162733869-03:00 | n/a | n/a (Access Denied page, 398 B) |
| BEJAIA (candidate) | https://univ-bejaia.dz/revue/jslcs/article/view/394 | 000 (no HTTP response) | 2026-11-05T12:44:22,162661969-03:00 | n/a | n/a (TLS verify failure, curl rc 60) |

## S962 sha mismatch — cause

Byte-level diff of the fresh body against `reports/round-93/evidence/S962.html` is a
single line:

```
- <input type="hidden" name="csrfToken" value="fb2501f7a93b4858b3b289b634904211" />
+ <input type="hidden" name="csrfToken" value="58759ad460c7dd57ab4024ce98ec1f26" />
```

(the second fetch produced `7b661293b5ca67fdc1b463eed88ba25c`; see the diff command output
in the report). Normalized text of the two bodies is byte-identical:
both 9727 characters, `equal_text True`. The difference is a per-session CSRF nonce, not
content. A second independent fetch produced yet another nonce and a third distinct
sha256 (`d443b9d5ce07c2dac32271a7e823ed24b6c33d18b4f671a4bf456bc0448cca4e`), with the
quote located again. The capture sha256 in `manifest.json` matches the capture file on
disk exactly (`098eed5c...`), so the capture is intact; the page is simply dynamic.

## Reachable-row context spans (from the fresh opens)

- S961: "...one type of politeness in particular, namely the speech acts of greeting and
  leave-taking denoted by the German verb grüssen."
- S962: "...greeting formulas derivated from the atelic predicate besar las manos (y los
  pies) 'to kiss the hands (and feet)', which, despite their apparent formal resemblance,
  came to codify totally opposite socio-pragmatic values."
- S963: "...due to pervasive contact between Ngoni and Swahili, greetings tend to be brief
  today and there is a widespread use of code-switching by all age groups."
- S964: "...elicited situationally bound responses and compiled a pool of words, expressions,
  and sayings that speakers reported using when saying goodbye to both acquaintances and
  strangers."

## Unreachable candidates — what the response was

- MDPI: HTTP 403, body is an Akamai "Access Denied" page
  (`<H1>Access Denied</H1>`, `You don't have permission to access ...`, Akamai error
  reference `18.6f11502.1793893462.7dcd936b`). Identical in shape to the captured
  `reports/round-93/evidence/unreachable-mdpi-403.raw`; only the Akamai error reference
  string differs (capture: `18.6f11502.1793891533.7d487a28`). UNREACHABLE — no bypass attempted.
- BEJAIA: no HTTP response at all. `curl: (60) SSL certificate OpenSSL verify result:
  unable to get local issuer certificate (20)`. Independent confirmation with
  `openssl s_client -connect univ-bejaia.dz:443 -servername univ-bejaia.dz` (verification
  left ON): `verify error:num=20:unable to get local issuer certificate`,
  `verify error:num=21:unable to verify the first certificate`,
  `subject=CN=*.univ-bejaia.dz issuer=C=US, O=Let's Encrypt, CN=YR1`,
  `Verify return code: 21`. The server does not send the intermediate certificate, so the
  chain cannot be built. No `-k`, no TLS bypass. UNREACHABLE.
