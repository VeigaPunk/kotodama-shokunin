# Round 64 W2 — final staged-row URL safety

Axes: **coverage**, **operability**, **calibration**.

## Scope and result

Read all 32 final `row.txt` files (S718–S749): 32 primary/live URLs and 26 concrete same-page capture URLs in mined rows S718–S743. Disposition rows S744–S749 have no capture URL except S748's `[UNRESOLVED]` placeholder. There are 24 distinct URL hostnames, including the capture host. DNS answers for every hostname were checked with `getent ahosts`; every returned IPv4/IPv6 address is globally routable. No private, loopback, link-local, ULA, unspecified, or metadata-service address was found, and no source URL uses a literal IP address.

Credential-like query-key and URL-userinfo searches across the staged row files found no matches. Concrete query parameters are non-secret identifiers/options: `id` (S726, S729, S737), `lang=en` (S741), and S744's test URL `q=ushanka`, `noredirect=true`, `mismatchType=misspelling`. No row was edited; no tool was installed.

## Host table

DNS answers were resolved on 2026-10-23. Representative addresses are shown; when a host returned multiple answers, all observed answers were checked and were public/global. `web.archive.org` is the capture host for S718–S743.

| Host | Row(s) | Representative DNS answer(s) | Classification |
|---|---|---|---|
| `pmc.ncbi.nlm.nih.gov` | S718, S720–S722, S725, S731–S734 | `2600:1901:0:c831::`, `34.107.134.59` | Public |
| `web.archive.org` | captures S718–S743 | `207.241.237.3` | Public |
| `pure.mpg.de` | S719 | `134.76.28.253` | Public |
| `www.nottingham.ac.uk` | S723 | `185.18.139.133` | Public |
| `ecampusontario.pressbooks.pub` | S724 | `108.139.163.3` (also `.126`, `.21`, `.86`) | Public |
| `eric.ed.gov` | S726, S737 | `165.224.128.227` | Public |
| `www.cambridge.org` | S727 | `104.17.111.190`, `104.17.110.190` | Public |
| `press-files.anu.edu.au` | S728 | `130.56.66.157` | Public |
| `journals.plos.org` | S729 | `35.190.43.188` | Public |
| `www.psych.mcgill.ca` | S730 | `132.216.44.143` | Public |
| `www.ling.ohio-state.edu` | S735 | `164.107.176.6` | Public |
| `www.frontiersin.org` | S736 | `2603:1061:14:121::1`, `150.171.110.35` | Public |
| `eprints.bbk.ac.uk` | S738 | `137.135.254.165` | Public |
| `journal.uny.ac.id` | S739 | `2405:b40:1:2::baca:a127`, `101.203.168.74` | Public |
| `online.ucpress.edu` | S740 | `104.18.12.179`, `104.18.13.179` | Public |
| `www.scielo.br` | S741 | `2400:52e0:1690::1160:1`, `138.199.4.179` | Public |
| `files.eric.ed.gov` | S742 | `2600:9000:24d5:d600:18:b473:4f00:93a1`, `13.33.4.96` | Public |
| `journals.linguisticsociety.org` | S743 | `135.148.34.95` | Public |
| `www.dictionary.com` | S744 (including TEST redirect) | `2a06:98c1:3108::ac40:9182`, `104.18.42.126` | Public |
| `www.merriam-webster.com` | S745 | `2606:4700:10::ac42:96c4`, `172.66.150.196` | Public |
| `en.wikisource.org` | S746 | `2a02:ec80:700:ed1a::1`, `195.200.68.224` | Public |
| `www.britannica.com` | S747 | `104.18.5.110`, `104.18.4.110` | Public |
| `penelope.uchicago.edu` | S748 | `128.135.102.61` | Public |
| `en.wikipedia.org` | S749 | `2a02:ec80:700:ed1a::1`, `195.200.68.224` | Public |

## New/re-source URL HEAD checks

Issued `curl -sI --max-time 30` (no redirect following) for the added S723/S740 URL pairs and the S729 re-source candidate pair. All six requests completed within the per-request timeout. Responses exposed no private redirect target.

| Row | URL | HTTP | Peer IP | Redirect |
|---|---|---:|---|---|
| S723 | `https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html` | 200 | `185.18.139.133` | none |
| S723 | `https://web.archive.org/web/20260324122540id_/https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html` | 200 | `207.241.237.3` | none |
| S729 | `https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518` | 200 | `35.190.43.188` | none |
| S729 | `https://web.archive.org/web/20261002073140id_/https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0151518` | 200 | `207.241.237.3` | none |
| S740 | `https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early` | 403 | `104.18.12.179` | none |
| S740 | `https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early` | 200 | `207.241.237.3` | none |

## Findings

### F1 — No unsafe URL target or credential disclosure path observed

- **Severity:** None; no URL-safety defect found.
- **Exploit path:** None observed. URL hosts resolve only to public addresses; no userinfo or credential-like query key was found.
- **Evidence:** 32 row files scanned; host table and query/userinfo scans above.
- **Impact:** No SSRF-style private/local fetch target or URL-carried credential exposure was identified in this staged surface.
- **Smallest remediation:** None. Leave row URLs unchanged.

### F2 — S740 live URL returns a plain-client 403

- **Severity:** Informational / low availability limitation; not a private-target or credential issue.
- **Exploit path:** An ordinary client opening the S740 live publisher URL may receive the Cloudflare 403 response. No challenge was bypassed; the same-page archive URL returned 200.
- **Evidence:** HEAD results above; S740's ACCESS line also records the live 403 and archive capture evidence.
- **Impact:** Direct access to the live page may be blocked for plain clients; the cited archive URL was reachable in this check.
- **Smallest remediation:** None for URL safety. Retain the accurate ACCESS note and same-page capture; do not bypass the challenge.

### F3 — S748 has no concrete capture target to classify

- **Severity:** Low assurance limitation; no unsafe target observed.
- **Exploit path:** None evidenced; the row contains a public live URL but only `[UNRESOLVED]` for capture.
- **Evidence:** S748 `ROW` capture field and TEST URL; live hostname resolves to `128.135.102.61`.
- **Impact:** This scan cannot classify or probe a future capture URL that is not present in the row.
- **Smallest remediation:** If a concrete capture URL is added later, repeat the same host/query/HEAD checks for that URL.

Report: .ufo/waves/round-64/w2/UrlSafetyFinal.md
