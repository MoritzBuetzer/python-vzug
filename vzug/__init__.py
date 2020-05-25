"""Base details for the V-ZUG Python bindings."""
import json
from typing import Any

import requests
from requests.auth import HTTPDigestAuth

from .constants import TIMEOUT, USER_AGENT, CONTENT_TYPE_JSON, CONTENT_TYPE, CONTENT_TYPE_TEXT_PLAIN

async def make_call(
    self,
    uri: str,
    username: str,
    password: str,
) -> Any:
    """Handle the requests to the V-ZUG unit."""

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": f"{CONTENT_TYPE_JSON}, {CONTENT_TYPE_TEXT_PLAIN}, */*",
    }

    if self._session is None:
        self._session = requests
        self._close_session = True
    
    response = self._session.get(uri, headers=headers, auth=HTTPDigestAuth(username, password), timeout=TIMEOUT)

    if CONTENT_TYPE_JSON in response.headers.get(CONTENT_TYPE, ""):
        response_json = await response.json()
        return response_json

    return response.text