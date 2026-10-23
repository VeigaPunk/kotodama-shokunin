# Round 64 w1 — staged URL safety audit

## Result and scope

Read-only audit of staged row URLs S718–S749, including disposition rows S744–S749. There are 30 `row.txt` files present: S723 and S740 were absent on three directory checks and have no URL to inspect. **No REFUSED-grade URL was found among the 30 staged rows; the range is not fully certifiable until S723 and S740 are audited.** No row was modified.

All 30 present primary locators use `https://`. URL material was scanned for credentials/userinfo, query secrets/session parameters, and non-web schemes. No credentials, tokens, or session identifiers were found in URLs. The only query values found are record/DOI identifiers (`S726`, `S729`, `S737`), `lang=en` (`S741`), and the S744 test URL's `q=ushanka`, `noredirect=true`, and `mismatchType=misspelling`; these are not credentials or session parameters. The archive URLs are plain `http`/`https` web URLs. No `file:`, `gopher:`, `ftp:`, `javascript:`, or `data:` URL was found. No URL userinfo (`user:pass@host`) was found.

Hostnames were checked with `getent ahosts`; every returned address was globally routable, not loopback, RFC1918/private, link-local, reserved, unspecified, or metadata-service space. The table shows the peer IP actually contacted by the HEAD request (one address; CDN/DNS may return other public addresses).

## Host table and HEAD results

Each request was `curl -sI --max-time 30 --show-error --write-out '\nstatus=%{http_code} remote_ip=%{remote_ip} redirect_url=%{redirect_url}\n' 'URL'`. No `-L` was used, so redirects were not followed. All requests completed within the 30-second per-request limit.

| Row(s) | Host | Observed peer IP | HEAD result |
|---|---|---|---|
| S718, S720–S722, S725, S731–S734 | `pmc.ncbi.nlm.nih.gov` | `2600:1901:0:c831::` | 200 |
| S719 | `pure.mpg.de` | `134.76.28.253` | 200 |
| S724 | `ecampusontario.pressbooks.pub` | `108.139.163.3` | 403 |
| S726, S737 | `eric.ed.gov` | `165.224.128.227` | 200 |
| S727 | `www.cambridge.org` | `104.17.111.190` | 429 |
| S728 | `press-files.anu.edu.au` | `130.56.66.157` | 200 |
| S729 | `journals.plos.org` | `35.190.43.188` | 200 |
| S730 | `www.psych.mcgill.ca` | `132.216.44.143` | 200 |
| S735 | `www.ling.ohio-state.edu` | `164.107.176.6` | 200 |
| S736 | `www.frontiersin.org` | `2603:1061:14:128::1` | 200 |
| S738 | `eprints.bbk.ac.uk` | `137.135.254.165` | 200 |
| S739 | `journal.uny.ac.id` | `2405:b40:1:2::baca:a127` | 200 |
| S741 | `www.scielo.br` | `2400:52e0:1690::1159:1` | 200 |
| S742 | `files.eric.ed.gov` | `2600:9000:24d5:6a00:18:b473:4f00:93a1` | 200 |
| S743 | `journals.linguisticsociety.org` | `135.148.34.95` | 200 |
| S744 | `www.dictionary.com` | `2a06:98c1:3101::6812:2a7e` | 301; `Location` is `https://www.dictionary.com/browse/khanka?q=ushanka&noredirect=true&mismatchType=misspelling`, same public host |
| S745 | `www.merriam-webster.com` | `2606:4700:10::6814:2dc7` | 403; `cf-mitigated: challenge` |
| S746 | `en.wikisource.org` | `2a02:ec80:700:ed1a::1` | 200 |
| S747 | `www.britannica.com` | `104.18.5.110` | 403; `cf-mitigated: challenge` |
| S748 | `penelope.uchicago.edu` | `128.135.102.61` | 200 |
| S749 | `en.wikipedia.org` | `2a02:ec80:700:ed1a::1` | 200 |

The 403 and 429 responses are access/rate-limit outcomes, not private-host findings. The Merriam-Webster and Britannica Cloudflare challenges were not bypassed. The only observed redirect was S744's same-host redirect to the Khanka headword; it does not target a private address. No other HEAD response exposed a redirect target.

The server responses included `Set-Cookie` headers on some requests. Those response values were not sent with requests, stored, replayed, or copied into this report; there was no curl config or netrc file and `CURL_HOME` was unset. They are not parameters in the staged URLs.

## Findings

### F1 — Two rows missing from the audited surface

- **Severity:** Low; incomplete assurance, not an observed unsafe URL.
- **Exploit path:** None evidenced for present rows. S723 and S740 have no staged record, so their eventual URLs cannot be classified here.
- **Evidence:** Three listings of `.ufo/waves/round-64/rows/` lacked `ScribeRowS723/row.txt` and `ScribeRowS740/row.txt`.
- **Impact:** Only 30 of the requested 32 row IDs can be certified against private-host, URL-secret, scheme, and response-header hazards.
- **Smallest remediation:** Once S723 and S740 are staged, run this same URL-only check on those two locators before reviewer reopening.

### F2 — No unsafe target found in the staged records

- **Severity:** None / no safety finding for the 30 present rows.
- **Exploit path:** None observed: all contacted peers were public addresses, the sole redirect stayed on `www.dictionary.com`, and no source URL contained credentials or session material.
- **Evidence:** Host table and 30 `curl -sI` status/peer-IP results above; scheme and query scan above.
- **Impact:** No SSRF-style private/local fetch path or URL credential exposure was identified in the records actually staged.
- **Smallest remediation:** None for URL safety; leave the rows unchanged. Do not retry through or bypass the noted access challenges as part of this audit.
