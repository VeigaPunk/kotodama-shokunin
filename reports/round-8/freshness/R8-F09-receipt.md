# R8-F09 freshness receipt — Mishnah Sotah 7:6 divine-name writing/reading/register distinction

- **Round:** 8 · **baseline_revision:** `e7ca0faeb6680fa9891b907be628d9db578c28f4` · **receipt_head:** `cf338a713060f274269cdacb18cdc0085bb06aeb`
- **Target:** `reports/round-8/targets.json` freshness[8] · **prior row:** R6-08-A (round-6 disposition: `partial-support`)
- **Entry:** `corpus/knowledge/civilizations/israel-ancient-hebrew.md` (locators: lines 107, 112, 113, 114; section 3 line 55)
- **Entry sha256 at receipt:** `f25a4b4066f6172afc697a279854ee85ed8a01ee1efdf00097e1d418ed1e80aa` — identical to the round-6 baseline hash; entry bytes unchanged.
- **Raw worker label:** `partial-support` (preserved verbatim; no reconciled disposition is asserted here — that belongs to `reports/round-8/freshness/reconciliation.json`).
- **Accessed:** 2026-10-17 (UTC session recorded 2026-10-17T20:14:12Z).

## Question (fixed)

Check the entry's divine-name writing/reading/register distinction against a located textual or scholarly source; retain textual-date and transmission limits, not a recovered universal ancient pronunciation.

## Main retrieval — primary text (entry-cited URL)

- **URL:** <https://he.wikisource.org/wiki/%D7%9E%D7%A9%D7%A0%D7%94_%D7%A1%D7%95%D7%98%D7%94_%D7%96_%D7%95>
- **Kind:** primary-text (Mishnah, Seder Nashim, Sotah 7:6, Hebrew Wikisource public-domain transcription)
- **Locator:** mishnah proper, second sentence, displayed in three parallel versions (unpointed; “משנה מנוקדת” pointed; “נוסח הרמב״ם” Maimonides codex), plus two commentaries on the same page (Rambam; Bartenura).
- **Passage (pointed version):**

  > בַּמִּקְדָּשׁ אוֹמֵר אֶת הַשֵּׁם כִּכְתָבוֹ, וּבַמְּדִינָה בְּכִנּוּיוֹ

  Worker gloss: “In the Temple he utters the Name as it is written, and in the province by its substitute.” (This gloss is the worker's, **not** Danby's.)
- **Commentary passages on the same page:**
  - Rambam ad loc.: `ככתבו - הוא הדבר הנקרא מיו״ד ה״א וי״ו ה״א וזהו שם המפורש הגדול` … `וכינויו - הוא אותו שאנו קוראין היום` (written form = yod-he-vav-he; substitute = “what we read today”).
  - Bartenura ad loc.: `בכנויו - באל״ף דל״ת` … `שאין מזכירין השם בכתבו אלא במקדש בלבד` (substitute = the name beginning alef-dalet, i.e. Adonai; written form mentioned only in the Temple).
- **Same-page gesture/place sentence** (entry line 107 row also claims gesture rules): `במדינה כהנים נושאים את ידיהן כנגד כתפיהן, ובמקדש על גבי ראשיהן, חוץ מכהן גדול שאינו מגביה את ידיו למעלה מן הציץ`.
- **Reproducible receipt:** `curl -sS -m 45 -w 'HTTP_STATUS:%{http_code} BYTES:%{size_download}' -o /tmp/hews_sotah76.html <url>` → `HTTP_STATUS:200 BYTES:101944`, sha256 `a8b4c8007ee9e5987e803ab102f6bddcf6c6c0712317946958897038ef9a332f`.
- **Retained limit:** the page is marked `לא בדוק` (not proofread) and shows three textual versions with minor variance; the citation is to the displayed standard text, not a named manuscript.

## Corroboration retrieval — reference work (entry's own cited source)

- **URL:** <https://www.jewishencyclopedia.com/articles/11305-names-of-god> — Jewish Encyclopedia (1901–1906), “Names of God”. New round-8 live retrieval of the same URL the round-6 receipt used for corroboration.
- **Reproducible receipt:** curl → `HTTP_STATUS:200 BYTES:131972`, sha256 `84cb281cf1865eceb42af55bdb05e73faf6852e74c88a59d4804040192efa40f`.

| Leg | Locator | Quoted passage | What it supports |
|---|---|---|---|
| qere perpetuum (entry line 113) | § “YHWH”, 3rd sentence | “the Masorites have inserted in the text, indicating thereby that Adonai was to be read (as a “ḳeri perpetuum”) instead of Yhwh” | Masoretic pointing cues a substitute reading, not a pronunciation from YHWH's consonants |
| “Jehovah” caveat (line 114) | § “YHWH”, 2nd sentence | “commonly represented … by the form “Jehovah,” which, however, is a philological impossibility” | “Jehovah” is not an independently recovered pronunciation |
| “the Name” / HaShem leg (line 113) | § “The Name”, 1st sentence | “it was known in the earliest rabbinical works simply as the Name” | The avoidance designation is “the Name” (Shem); “HaShem” itself is the entry's modern-Hebrew gloss — the JE article text does not use the term (only the bibliography title “Sefer ha-Shem”) |
| Temple priests vs Adonai outside | § “The Name”, sentence citing Soṭah vii. 6 | “The pronunciation of the written Name was used only by the priests in the Temple … outside the Temple they used the title “Adonai” (Soṭah vii. 6; p. 38a)” | Cross-confirms Sotah 7:6 from the entry's cited reference work |
| no recovered pronunciation | § “Ehyeh-Asher-Ehyeh”, opening | “After the destruction of the Second Temple there remained no trace of knowledge as to the pronunciation of the Name” | The transmission limit the entry keeps: no recovered Iron Age pronunciation |

## Translation-layer retrievals (kept separate from the Hebrew text)

- **mishnah.org (entry-cited):** <https://www.mishnah.org/learn/sotah/7/6/> → curl `HTTP_STATUS:200 BYTES:120881`, sha256 `9c5b7161fdd5cfa0e6c258257c8f32be325eba1a61b3c830a3af8b7d18ad8964`. Sentence: “In the Temple, the priest utters the name of God as it is written in the Torah, i.e., the Tetragrammaton, and in the country they use its substitute name of Lordship.” Sweep: `grep -o -i 'Danby'` → 0 matches (supports the entry's “do not attribute to Danby” caution).
- **Sefaria API:** <https://www.sefaria.org/api/texts/Mishnah_Sotah.7.6?context=0&commentary=0> → HTTP 200, 12575 bytes, exit 0. English versionTitle “William Davidson Edition - English” (CC-BY-NC); Hebrew “Torat Emet 357” (public domain). The English sentence is word-identical to the mishnah.org sentence (shared source inferred from identical wording, not asserted by mishnah.org). Round-6 recorded a failed Sefaria attempt; this round's API call succeeded.

## Documented access attempt — entry-cited grammar (still unread)

- **Jouon–Muraoka 2006** (entry line 114 citation): <https://books.google.com/books?vid=ISBN9788876536298> returned only the publisher blurb/author biography — an identity-level record, not a passage. The grammar's own wording remains unread; the pointing-cue claim is supported this round only at JE reference-work level.

## Negative sweeps (commands + date 2026-10-17)

- JE article: `grep -o -i 'Iron Age'` → 0 matches (the article makes no Iron Age pronunciation claim); `grep -o -i 'hashem|ha-shem'` → 1 match = bibliography title “Sefer ha-Shem”, not the term HaShem.
- mishnah.org page: `grep -o -i 'Danby'` → 0 matches.
- Wikisource page: `כִּכְתָבוֹ` → 1; `בְּכִנּוּיוֹ` → 1; `לא בדוק` → 1; `נוסח הרמב` → 2.
- `ls reports/round-8/` at receipt time: `claims.json depth freshness operability targets.json` — `run-validation.py` not yet authored (O-shard pending); this receipt is filed for it, not validated by it.

## Support scope — passage support vs whole-claim support

**Supported this round (reception-layer legs):** the Sotah 7:6 written-name/Temple vs substitute/province distinction (primary text, re-verified live, with two medieval glosses); the qere perpetuum leg; the “the Name” designation leg; the pointing-cue / “Jehovah” caveat; the no-recovered-pronunciation limit.

**Not established (kept as limits):** Jouon–Muraoka 2006 wording (unread); Danby 1933 (not inspected); the Mishnah's c. 200 CE dating (entry line 112 — not re-verified by any retrieved passage this round); a recovered Iron Age pronunciation or a universal ancient ban (nothing retrieved supports either; the entry claims neither).

**Verdict label (raw):** `partial-support` — the bounded question's reception-layer legs are now passage-confirmed with fresh quoted receipts; the citation-edition legs and the dating remain open.
