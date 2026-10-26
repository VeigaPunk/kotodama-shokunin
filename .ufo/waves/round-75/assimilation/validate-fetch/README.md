# validate-fetch — fetch receipts for the round-75 SCRATCHMIRROR rehearsal

Each `.meta` file is one fetch record. Format (tab-separated):

```
<id>\t<HTTP status> <bytes> <content-type> <effective url>\t<sha256 of the fetched body>
```

The User-Agent on **every** request below was:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
```

(QUALITY 22: each User-Agent is bound to the response that request got.)

`urls.txt` is the id → URL list that was fetched.

| file | what it is |
|---|---|
| `S885.meta` `S886.meta` `S887.meta` | the three persee **document** pages (notice + first paragraph) — these carry the Gate quotes for S885/S886/S887 |
| `W891.meta` | unige.ch *S/Z* excerpt, read from the Internet Archive capture `20041220223357id_` (the live page served a bot challenge; met, not passed) |
| `S892.meta` | iris.unipa.it Marrone PDF, read from the Internet Archive capture `20251111222249if_` (the direct URL answered HTTP 403 to a plain request) |
| `S893.meta` | chinawriter 2023/0922 article (the S870 re-open) |
| `S888.meta` | jw.ucass Chinese narratology syllabus PDF |
| `S889.meta` | jstage `jcss/25/2/25_200` PDF |
| `S890.meta` | jstage `jsik/32/2/32_2022_017` PDF (the first plain request answered HTTP 502; the retry with a Referer answered 200) |


The nine mirror rows' anchor quotes are located in these bodies, and each is the SAME string the
lesson draft's `## Gate` carries for that row; the measurement is in
`../validate-receipt-draft.txt` (`== anchor-quote location …` and `== GATE cross-check …`).

The persee **document** pages are not byte-stable across fetches (same length, different sha256 —
the served page carries per-request content), so the sha256 above is the sha256 of the body this
seat stored. An evidence file must record the sha256 of its own fetch, and the window-sha256 must be
recomputed from the stored window.
