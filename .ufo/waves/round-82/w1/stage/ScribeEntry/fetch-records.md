# Fetch receipts — ScribeEntry (round 82, wave 1, claim D)

All probes run 2026-11-04 from scratch `/fast/scratch/hyaku/kotodama-r82/ScribeEntry/fetch/`; this record carries the commands, the UA-bound responses, the hashes and the located passages; the downloaded pages themselves stayed in scratch and are removed at yield. Every record binds the exact User-Agent to the response that request got. "wall absent" means the response contains article prose and none of the challenge markers `Just a moment`, `Enable JavaScript`, `Checking your browser`, `Cloudflare`; the string `captcha` does occur in MediaWiki site configuration on every Wikisource page including the successful positive control below, so it is not a wall marker. No challenge was passed, no login, paywall, geo block or captcha met.

## S904 — Homer, *Odyssey*, trans. Samuel Butler (Gutenberg #1727)

```text
$ curl -sS -A 'curl/8.23.0' -D hdr_1727.txt -o pg1727.txt -w 'HTTP %{http_code} %{size_download} B\n' https://www.gutenberg.org/cache/epub/1727/pg1727.txt
HTTP 200 717782 B
```

- UA "curl/8.23.0" -> HTTP 200, 717782 B, wall absent
- headers: `content-type: text/plain; charset=utf-8`, `content-length: 717782`, `server: Apache`, `date: Wed, 04 Nov 2026 11:12:23 GMT`
- sha256 `b167ce5e348bf805dfe4355dff2eae5c2e522b11cce003a6f98bb65a753bbc69`
- title block: `Title: The Odyssey` / `Author: Homer` / `Translator: Samuel Butler`
- edition date: line 304 `Butler's Translation of the “Odyssey” appeared originally in 1900`

Located passages (line numbers in the served file):

- 4018-4020 — supplication to Polyphemus: 「we are your suppliants, and Jove takes all respectable travellers under his protection」
- 4024-4029 — Polyphemus' refusal: 「We Cyclopes do not care about Jove or any of your blessed gods, for we are ever so much stronger than they」
- 3754 — Alcinous: 「he ought to treat a guest and a suppliant as though he were his own brother」
- 6152-6154 — Eumaeus: 「it would not be right for me to insult him, for all strangers and beggars are from Jove」
- 6613-6615 — Menelaus: 「One should treat a guest well as long as he is in the house and speed him when he wants to leave it」
- 6600-6601 — Pisistratus: 「So long as he lives a guest should never forget a host who has shown him kindness」
- 3648-3650 — Alcinous to Arete: 「set a copper on the fire and heat some water; our guest will take a warm bath」

## S905 — Tacitus, *Germania*, trans. Church and Brodribb (Wikisource)

```text
$ curl -sSL -A 'curl/8.23.0' -o germania.html -w 'HTTP %{http_code} %{size_download} B\n' 'https://en.wikisource.org/wiki/Germania_(Church_%26_Brodribb)'
HTTP 200 163266 B
```

- UA "curl/8.23.0" -> HTTP 200, 163266 B, wall absent
- sha256 `8138fd6ba5f20abd85c8e2d3de216960f0f79fad04b9a4b7c0d9281527182c49`
- page title block: `The Origin and Situation of the Germans (1876) by Tacitus, translated by Alfred John Church and William Jackson Brodribb`
- category: `1876 works`, `PD-old 98`

Located passage: chapter XXI, one paragraph. All seven quotes in the entry are substrings of it after whitespace normalisation. The chapter also states the no-return rule: 「they expect no return for what they give, nor feel any obligation for what they receive」.

## S906 — Ovid, *Metamorphoses* VIII-XV (Gutenberg #26073)

```text
$ curl -sS -A 'curl/8.23.0' -D hdr_26073.txt -o pg26073.txt -w 'HTTP %{http_code} %{size_download} B\n' https://www.gutenberg.org/cache/epub/26073/pg26073.txt
HTTP 200 853821 B
```

- UA "curl/8.23.0" -> HTTP 200, 853821 B, wall absent
- headers: `content-type: text/plain; charset=utf-8`, `content-length: 853821`
- sha256 `6eb477505c6e19bbefbe0d78ba5a9642f661d5cbbbc5f754bfb3e45bc611ba35`

Located passages (line numbers in the served file):

- 1648-1650 — 「To a thousand houses did they go, asking for lodging and for rest」
- 1650-1651 — 「Yet one received them, a small one indeed, thatched with straw」 (the source continues `,[84] and the reeds of the marsh`)
- 1674-1676 — the trough: 「this is filled with warm water, and receives their limbs to refresh them」
- 1700-1705 — the goblet and the hosts' apology: 「they are frightened, and, with hands held up, they offer their prayers, and entreat pardon for their entertainment」
- 1710-1711 — 「We are Divinities, and this impious neighbourhood shall suffer deserved punishment」
- 1727-1729 — the request: 「We desire to be your priests, and to have the care of your temple」

## S907 — "Guest", *Encyclopaedia Britannica*, 11th edn (Wikisource slug + archive capture)

Live slug, two User-Agents, same bytes:

```text
$ curl -sS -A 'curl/8.23.0' -o guest_plain.html -w 'plain: HTTP %{http_code} %{size_download} B\n' 'https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Guest'
plain: HTTP 200 60273 B
$ curl -sS -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -o guest_browser.html -w 'browser: HTTP %{http_code} %{size_download} B\n' 'https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Guest'
browser: HTTP 200 60273 B
```

- UA "curl/8.23.0" -> HTTP 200, 60273 B, wall absent; UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 60273 B, wall absent
- both responses byte-identical: sha256 `f6db75f387e95d9d83fc2515a09c4b3acfd66605fe876c995bd0c0c490b26718`
- **prose served, not a scaffold**: a full HTML parse of the `mw-content-text` container yields 318 words of visible text and the article sentence is present — `…cognate with Lat. hostis, originally a stranger, hence enemy; cf. “host”), one who receives hospitality in the house of another, his “host”; hence applied to a parasite.` The page also carries a raw Parsoid `data-mw` template payload before the paragraph; a naive tag-strip that starts at that payload can truncate the extraction, which is what an early probe of mine did before the full parse corrected it. The live slug is openable by ordinary means.

Archive capture (fixed copy for the row):

```text
$ curl -sSL -A 'curl/8.23.0' -o guest_wayback.html -w 'HTTP %{http_code} %{size_download} B\n' 'https://web.archive.org/web/20191023112911/https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Guest'
HTTP 200 29020 B
```

- UA "curl/8.23.0" -> HTTP 200, 29020 B, wall absent
- sha256 `37a3eb42b70863a5cd527128d57081895cc5c846b907c7aeb0be7535474b801d`
- `mw-parser-output` present; prose present, including `GUEST (a word common to Teutonic languages; cf. Ger. Gast, and Swed. gäst; cognate with Lat. hostis, originally a stranger, hence enemy; cf. "host"), one who receives hospitality in the house of another, his "host"; hence applied to a parasite.`

Positive control for the namespace (QUALITY 21+24): the same Wikisource 1911 Britannica namespace, a slug whose live page is a normal transcription:

```text
$ curl -sS -A 'curl/8.23.0' -o ordeal_control.html -w 'HTTP %{http_code} %{size_download} B\n' 'https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Ordeal'
HTTP 200 87131 B
```

- UA "curl/8.23.0" -> HTTP 200, 87131 B, wall absent
- sha256 `a9f748e651c7204a047303bba0086cafd483904798c3b9396de7f2a74645cbcf`
- `mw-parser-output` present, 3374 words of prose: the namespace renders prose, so the Guest scaffold is slug-specific and not a site-wide block.

## Opened but not cited

- Bellows, *The Poetic Edda*, Hovamol (Wikisource). UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 510701 B, wall absent, sha256 `a0427ccca3a52b115530720b4ef180a624ce701eb78af356daa3e2e6d2ddf98b`. Opened while the planned row set still had Hávámál as the second row; not cited after ScoutGap's duplicate-document finding (`SOURCES.md:349` S320 is the same Bellows translation) and the L1 row amendment that made the second row Tacitus, *Germania*.

## Scratch

All downloads and derived files live at `/fast/scratch/hyaku/kotodama-r82/ScribeEntry/fetch/`; the scratch tree is removed at yield. This stage directory holds only this record, the two checkers' outputs, the structure census, and the checker script.
