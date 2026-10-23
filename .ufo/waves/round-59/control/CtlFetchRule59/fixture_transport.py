"""Map only synthetic *.fixture.test URLs to loopback; never change fetch/locator behavior."""
import os
import urllib.parse
import urllib.request

_RAW_OPEN = urllib.request.urlopen

def install(origin, tag):
    def mapped(request, *args, **kwargs):
        url = request.full_url if hasattr(request, 'full_url') else str(request)
        parts = urllib.parse.urlsplit(url)
        synthetic = parts.hostname and parts.hostname.endswith('.fixture.test')
        archived_synthetic = parts.hostname == 'web.archive.org' and '.fixture.test' in parts.path
        if synthetic or archived_synthetic:
            headers = dict(request.header_items()) if hasattr(request, 'header_items') else {}
            headers.update({'X-Fixture-URL': url, 'X-Fixture-Run': tag})
            request = urllib.request.Request(origin + '/fetch', headers=headers, method='GET')
        return _RAW_OPEN(request, *args, **kwargs)
    urllib.request.urlopen = mapped

if os.environ.get('FETCH59_ORIGIN'):
    install(os.environ['FETCH59_ORIGIN'], os.environ.get('FETCH59_TAG', 'counter'))
