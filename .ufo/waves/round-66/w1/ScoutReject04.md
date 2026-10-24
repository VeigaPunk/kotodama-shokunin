# ScoutReject04 — REJECT-CANDIDATE: Japanese sari/incense robes airing tradition (S804)

## Verdict: ADMIT → row-S804.txt written

## Topic resolution
- "incense robes airing" resolves to the Japanese **mushiboshi / bakuryō** tradition: the annual airing of stored books, kimono and other textiles against mildew/insects (University of Illinois *Mushiboshi Project*; JAANUS *bakuryō*; Smithsonian NMAA object record).
- The "sari" element does not resolve to the Indian garment in a Japanese airing context (Shōsō-in *sari* 裂 = textile fragments is a different register); I treated it as unverified garnish and grounded the row on the museum-attested airing tradition itself.
- "(lead: museum)" satisfied: Smithsonian National Museum of Asian Art object record F1905.309 (Katsukawa Shunshō, *Women Airing Books and Clothes*), tier A.

## Chosen row (see rows/ScoutReject04/row-S804.txt)
- Live URL: `https://asia-archive.si.edu/object/F1905.309/` — Smithsonian official collection host, curl 200 today.
- Anchor quote (14 words, verbatim in label body): "The annual airing of books and clothing to prevent mildew and insects takes place each year in summer."
- Scent-entry fit: textile-storage ritual adjacent to takimono/kusudama scent-keeping of stored robes; adds new host `asia-archive.si.edu`.

## Evidence
- **Live verify:** `curl -sS -A Mozilla/5.0 https://asia-archive.si.edu/object/F1905.309/` → HTTP 200, 119946 B, quote present verbatim. Re-fetched via Wayback save.
- **Capture (fresh, not fabricated):** `web.archive.org/save/…` → 302 to `…/web/20261024113801/`; CDX now lists `20261024113801 200`. `id_` replay fetched 200 (33067 B gzip → 119909 B decoded); decoded body contains the quote verbatim. Older capture `20250331195524id_` (112686 B) also contains it — two independent replay confirmations.
- **Uniqueness:** `grep -rn "asia-archive.si.edu\|asia.si.edu\|F1905.309\|collections.si.edu" corpus/ .ufo/` — no SOURCES.md or fragment usage of this URL; only unrelated asia-archive educator-video link (tibet.md) and historical scout notes about 403s.
- **Access caveats recorded:** `asia.si.edu` (non-archive host) returns a JS "request verification" page to curl (403 challenge); `new.artsmia.org/living-rooms` (Mia Mushi Boshi section) is Vercel-bot-walled (429). Both rejected as live rows for re-opener fragility — the canonical archive host has no wall.
- archive.org was intermittently connection-refused during the session; all archive facts above come from successful CDX + id_ replay fetches, not inference.

## Rejected alternates (if integrator prefers rejects.txt semantics)
- `https://asia.si.edu/explore-art-culture/collections/search/edanmdm:fsg_F1905.309/` - 403 JS verification wall, quote not curl-readable; flip: host serves body text to plain curl.
- `https://new.artsmia.org/living-rooms` - Vercel security checkpoint (429 shell); flip: Vercel checkpoint removed/bypassed.
- `https://shosoin.kunaicho.go.jp/en-US/about/treasure/` - JS-rendered Nuxt shell, no body text via curl; flip: SSR or static body.
- `https://publish.illinois.edu/mushiboshi/a-worlds-eye-view-of-preservation/` - works (200, quote present) but tier weaker (university library project blog) and weaker museum fit; kept as fallback only.

## Gaps / notes for integrator
- Row drafted for slot **S804** only; the entry file `scent-perfume-aromatics-codes.md` is owned by ScribeEntrySpec — the ROW= line already names it in used-by.
- If the integrator wants the incense linkage tighter, the Met essay `https://www.metmuseum.org/essays/japanese-incense` (robes perfumed via takimono) exists but was not needed for this slot.
- No tools installed; curl/python3/pdftotext already present.
