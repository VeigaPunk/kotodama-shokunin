# ScribeRowS699 — Round 63 C source candidate

**Result: blocked; no S699 row is admissible yet.** I prepared the source row, entry bullet, and Gate-line drafts in scratch, but the required locator did not locate the quote from the Wayback capture. Do not merge the drafts into `corpus/SOURCES.md` or the entry as verified support.

## Behavior and evidence

Scope was the C-row S699 mitre source only. I read `reports/round-63/claims.json` (both full frozen predicate statements), both counter docstrings, and section 5 of `corpus/lessons/round-62-verifier-spotcheck.md` before source work. `sha256sum /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-63/accept-o.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-63/accept-c.py` returned the frozen hashes exactly:

```text
a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de  /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-63/accept-o.py
3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca  /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-63/accept-c.py
```

**Chosen page:** Joseph Braun, “Mitre,” *The Catholic Encyclopedia* (Robert Appleton Company), 1911: <https://www.newadvent.org/cathen/10404a.htm>. The exact 18-word quote is in the article body paragraph under “Form, material, and use,” not a caption or attribute:

> “The right to wear the mitre belongs by law only to the pope, the cardinals, and the bishops.”

Live locator command and complete output:

```text
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://www.newadvent.org/cathen/10404a.htm' 'The right to wear the mitre belongs by law only to the pope, the cardinals, and the bishops.' ; rc=$?; printf 'exit=%s\n' "$rc"
LOCATED https://www.newadvent.org/cathen/10404a.htm
exit=0
```

The ordinary CDX request succeeded:

```text
curl -sS -D - 'https://web.archive.org/cdx/search/cdx?url=www.newadvent.org%2Fcathen%2F10404a.htm&output=json&limit=-5&filter=statuscode%3A200'
HTTP/2 200
```

It returned five status-200 captures, each with the original URL exactly `https://www.newadvent.org/cathen/10404a.htm`, at timestamps `20260717015124`, `20260812203755`, `20260829053802`, `20260830220949`, and `20260831220821`. The latest candidate is <https://web.archive.org/web/20260831220821id_/https://www.newadvent.org/cathen/10404a.htm>. A static `read` of that capture returned the same article body and exact quote; ordinary `curl -sS -D - -o /dev/null 'https://web.archive.org/web/20260831220821id_/https://www.newadvent.org/cathen/10404a.htm'` returned HTTP/2 200 and `memento-datetime: Mon, 31 Aug 2026 22:08:21 GMT`.

However, the required base locator did **not** locate the quote in the archive. Exact command and output:

```text
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 300 python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260831220821id_/https://www.newadvent.org/cathen/10404a.htm' 'The right to wear the mitre belongs by law only to the pope, the cardinals, and the bishops.' ; rc=$?; printf 'exit=%s\n' "$rc"
NOT_LOCATED https://web.archive.org/web/20260831220821id_/https://www.newadvent.org/cathen/10404a.htm URLError
exit=1
```

The same quote on the older `20260812203755id_` capture returned `NOT_LOCATED … URLError`, exit 1; the display URL without `id_` for the latest capture also returned `NOT_LOCATED … URLError`, exit 1. A separate ordinary urllib diagnostic using the locator’s Firefox User-Agent observed `URLError(ConnectionRefusedError(111, 'Connection refused'))`. Cause unresolved. The locator failure is authoritative for this row requirement; the `read`/curl observations do not replace a locator pass. The live page itself was not blocked (live locator passed), so the “live 403, capture met-not-passed” exception does not apply.

### Draft artifacts — not accepted pending archive locator

**Registry row draft:**

```text
| S699 | Mitre, The Catholic Encyclopedia (Robert Appleton Company), 1911 - https://www.newadvent.org/cathen/10404a.htm ; capture https://web.archive.org/web/20260831220821id_/https://www.newadvent.org/cathen/10404a.htm | encyclopedia | B | Catholic Encyclopedia account of the mitre's form and regulated wear by ecclesiastical ranks | Form, material, and use, "The right to wear the mitre belongs by law only to the pope, the cardinals, and the bishops." | Braun describes the mitre's construction and identifies the church offices authorized to wear it. | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |
```

**Entry bullet draft:**

```text
- The right to wear the mitre rests with the pope, cardinals, and bishops under church law (S699)
```

This clause has eight content words under the stated length/stopword rule; `right`, `wear`, `mitre`, `pope`, `cardinals`, and `bishops` occur in the quote in order. Its longest verbatim run is six words (`The right to wear the mitre`), within the 12-word limit.

**Gate-line draft (not Gate-ready until archive locator passes):**

```text
- S699 | https://www.newadvent.org/cathen/10404a.htm | 2026-10-23 | "The right to wear the mitre belongs by law only to the pope, the cardinals, and the bishops."
```

The candidate URL had no match in `corpus/SOURCES.md` or in the already-present `.ufo/waves/round-63/w1/` reports when checked.

## Rejections

- Britannica’s `https://www.britannica.com/topic/miter` page was readable by static read and exposed a body-text quote, but its direct locator returned `NOT_LOCATED https://www.britannica.com/topic/miter HTTPError`, exit 1. Its CDX request returned HTTP/2 429 Too Many Requests (`x-rl: 0`, `x-na: 0`). Discarded; no row drafted from that page.
- An initial wrong-path New Advent URL, `https://www.newadvent.org/cathen/10317a.htm`, resolved to “Venerable Ralph Milner,” not a mitre article; discarded.

## Gates, surfaces, and limits

- **C row-local source checks:** live locator PASS; same-page CDX capture exists and its body quote is visible through `read`; archive locator FAIL/NOT_LOCATED. Therefore S699 is not confirmed on both URLs and is not submitted as an accepted row.
- **Full `ACCEPT-C-63` counter:** not run; this seat did not edit the entry or registry and cannot claim the frozen C predicate.
- **Claim O / safety hold:** out of scope; no repair, review, counter, or live use of `tools/reopen-row.py` was performed.
- **Touched surfaces:** this scoped report and the scratch artifacts listed below only. No lane registry, knowledge entry, counter, product code, or other report was changed. No tool was installed or updated.
- **Known limit:** archive content is present in the static read and direct curl succeeds, but the required locator’s ordinary urllib fetch is refused. A different source with a locator-confirmed capture, or ordinary locator connectivity that allows this capture fetch, is still required before this source can be used.

## Artifact paths

- Report: `.ufo/waves/round-63/w1/ScribeRowS699.md`
- Scratch drafts and full locator/CDX transcript:
  - `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS699/S699-registry-row.txt`
  - `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS699/S699-entry-bullet.txt`
  - `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS699/S699-gate-line.txt`
  - `/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-ScribeRowS699/S699-locator-cdx.txt`
