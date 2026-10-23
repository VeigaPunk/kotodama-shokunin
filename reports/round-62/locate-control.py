#!/usr/bin/env python3
r"""Round-62 paired recovery/exhaustion control for claim D's LOCATE leg (QUALITY criterion 13: a
bounded fetch treatment has its own control). Run from the lane root:

  python3 -B reports/round-62/locate-control.py

It imports reports/round-62/accept-d.py (locate_row, PASSES, GAP) and the base locator
reports/round-61/reopen-quote.py unchanged, replaces only the locator's network call (fetch), its
host refusal (url_refusal; the fixture hosts are fictitious) and every sleep with a virtual clock,
and runs scripted outcomes per URL and attempt. Each case prints PASS or FAIL against its expected
verdict, request counts and virtual waits; the last line is `LOCATE-CONTROL-62: PASS|FAIL`.
Cases:
  RECOVER    live 403 every time; capture 503,503,503 in pass 1, a connection error in pass 2, 200
             with the quote in pass 3 -> located in pass 3; live 3 requests, capture 3+1+1
  EXHAUST    live 403; capture 503 on every attempt -> NOT located after 3 passes; live 3, capture 9;
             two 60 s pass waits
  ABSENT     live 200 without the quote on every pass, capture 200 without the quote -> NOT located;
             live 3, capture 3 (no transient retry inside a pass)
  FIRSTOK    live 200 with the quote -> located in pass 1; live 1, capture 0; no pass wait
  CAPTUREOK  live 403; capture 200 with the quote -> located in pass 1; live 1, capture 1
  DNSFAIL    live and capture raise a name-resolution error every time -> NOT located; 1 request
             per URL per pass (fetch() does not retry URLError), 3 each in total
"""
import importlib.util
import os
import sys
import urllib.error

ROOT = os.getcwd()
QUOTE = "the wings or winged sandals on the feet of a fixture god named here"
LIVE = "https://example-live.invalid/talaria"
CAP = "https://web.archive.org/web/20240529024530id_/https://example-live.invalid/talaria"
BODY_OK = f"<html><body><p>{QUOTE}.</p></body></html>".encode()
BODY_NO = b"<html><body><p>an unrelated page about other matters entirely</p></body></html>"


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def http_error(url, code):
    return urllib.error.HTTPError(url, code, "scripted", {}, None)


def main():
    acc = load("accept_d", "reports/round-62/accept-d.py")
    loc = load("reopen_quote", "reports/round-61/reopen-quote.py")
    results = []

    def case(name, script, want_ok, want_counts, want_pass_waits):
        counts = {LIVE: 0, CAP: 0}
        clock = {"t": 0.0, "pass_waits": 0}

        def fake_fetch(url):
            # mirrors the base fetch(): up to 3 attempts on 429/5xx with a sleep between, else raise
            for attempt in (1, 2, 3):
                counts[url] += 1
                outcome = script(url, counts[url])
                if isinstance(outcome, bytes):
                    return outcome, "text/html"
                if isinstance(outcome, urllib.error.HTTPError) and outcome.code in (429, 500, 502, 503, 504, 508, 520, 522, 524) and attempt < 3:
                    clock["t"] += 8
                    continue
                raise outcome
            raise AssertionError("unreachable")

        def pass_sleep(seconds):
            clock["t"] += seconds
            clock["pass_waits"] += 1

        loc.fetch = fake_fetch
        loc.url_refusal = lambda url, quote: ""
        ok, why, used = acc.locate_row(loc, [LIVE, CAP], QUOTE, passes=acc.PASSES, gap=acc.GAP, sleep=pass_sleep)
        got_counts = (counts[LIVE], counts[CAP])
        good = ok == want_ok and got_counts == want_counts and clock["pass_waits"] == want_pass_waits
        results.append(good)
        print(f"{name} {'PASS' if good else 'FAIL'} located={ok} passes_used={used} requests(live,capture)={got_counts} "
              f"want={want_counts} pass_waits={clock['pass_waits']} virtual_s={clock['t']:.0f} detail={why[:160]}")

    def recover(url, n):
        if url == LIVE:
            return http_error(url, 403)
        if n <= 3:
            return http_error(url, 503)
        if n == 4:
            return urllib.error.URLError("connection reset (scripted)")
        return BODY_OK

    case("RECOVER", recover, True, (3, 5), 2)
    case("EXHAUST", lambda u, n: http_error(u, 403) if u == LIVE else http_error(u, 503), False, (3, 9), 2)
    case("ABSENT", lambda u, n: BODY_NO, False, (3, 3), 2)
    case("FIRSTOK", lambda u, n: BODY_OK if u == LIVE else BODY_NO, True, (1, 0), 0)
    case("CAPTUREOK", lambda u, n: http_error(u, 403) if u == LIVE else BODY_OK, True, (1, 1), 0)
    case("DNSFAIL", lambda u, n: urllib.error.URLError("name resolution failed (scripted)"), False, (3, 3), 2)
    verdict = all(results)
    print(f"LOCATE-CONTROL-62: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
