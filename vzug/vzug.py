"""A Python Client to get Infos from V-ZUG devices."""
import logging
import json
import requests
from yarl import URL

from . import make_call
from .constants import (
  API,
  API2,
  DEVICE_STATUS, PROGRAM_STATUS,
)

_LOGGER = logging.getLogger(__name__)

class VZUG:
    """A class for handling the communication with a V-ZUG device."""

    def __init__(self, host: str, username: str, password: str, session: requests.Session() = None) -> None:
        """Initialize the devices."""
        self._host = host
        self._username = username
        self._password = password
        self._session = session
        self._device_status = None
        self._program_status = None
        self.uri: URL = URL.build(scheme="http", host=self._host)
        print(self.uri)

    async def get_device_status(self) -> None:
        """Get the details from the devices."""
        url = self.uri.join(API).update_query({'command': DEVICE_STATUS})
        response = await make_call(self, uri=url, username=self._username, password=self._password)
        self._device_status = response

    async def get_program_status(self) -> None:
        """Get information about the currently running program"""
        url = self.uri.join(API2).update_query({'command': PROGRAM_STATUS})
        response = await make_call(self, uri=url, username=self._username, password=self._password)
        self._program_status = response

    @property
    def device_status(self) -> str:
        """Return the current device details."""
        return self._device_status

    @property
    def program_status(self) -> str:
        """Return the current program details."""
        return self._program_status

    # See "Using Asyncio in Python" by Caleb Hattingh for implementation details.
    async def close(self) -> None:
        """Close an open client session."""
        if self._session and self._close_session:
            await self._session.close()

    async def __aenter__(self) -> "VZUG":
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""