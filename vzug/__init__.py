"""Base details for the vzug Python bindings."""
import asyncio
import json
import socket
from typing import Any, Mapping, Optional

import aiohttp
import async_timeout

from .constants import TIMEOUT, USER_AGENT, CONTENT_TYPE_JSON, CONTENT_TYPE, CONTENT_TYPE_TEXT_PLAIN
from .exceptions import VZUGConnectionError, VZUGError


async def make_call(
    self,
    uri: str,
    method: str = "GET",
    data: Optional[Any] = None,
    json_data: Optional[dict] = None,
    parameters: Optional[Mapping[str, str]] = None,
    token: str = None,
) -> Any:
    """Handle the requests to the dingz unit."""

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": f"{CONTENT_TYPE_JSON}, {CONTENT_TYPE_TEXT_PLAIN}, */*",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    if self._session is None:
        self._session = aiohttp.ClientSession()
        self._close_session = True

    try:
        with async_timeout.timeout(TIMEOUT):
            response = await self._session.request(
                method, uri, data=data, json=json_data, params=parameters, headers=headers,
            )
    except asyncio.TimeoutError as exception:
        raise VZUGConnectionError("Timeout occurred while connecting to vzug unit") from exception
    except (aiohttp.ClientError, socket.gaierror) as exception:
        raise VZUGConnectionError("Error occurred while communicating with vzug") from exception

    if CONTENT_TYPE_JSON in response.headers.get(CONTENT_TYPE, ""):
        response_json = await response.json()
        return response_json

    return response.text