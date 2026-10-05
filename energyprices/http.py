"""The job's single network entry point. Tests replace `get` with a raising stub."""

import ssl
import urllib.error
import urllib.parse
import urllib.request

import certifi

TIMEOUT_S = 60
USER_AGENT = "energyprices-job/1 (+private)"

# uv's standalone Python has no system trust store on macOS; certifi works everywhere.
_TLS = ssl.create_default_context(cafile=certifi.where())


class FetchError(Exception):
    """A source could not be read. The message never contains the request URL,
    because some sources carry their token in the query string."""


def get(url: str, params: dict | None = None, headers: dict | None = None) -> bytes:
    full = url + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(full, headers={"User-Agent": USER_AGENT, **(headers or {})})
    host = urllib.parse.urlsplit(url).netloc
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S, context=_TLS) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        # The body of an error page can echo the query, so only its status is reported.
        raise FetchError(f"{host}: HTTP {e.code}") from None
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        reason = getattr(e, "reason", e)
        raise FetchError(f"{host}: {type(e).__name__}: {reason}") from None
