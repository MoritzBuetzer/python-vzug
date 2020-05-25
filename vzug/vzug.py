"""A Python Client to interact with V-ZUG devices"""
import logging
import json
import aiohttp
from yarl import URL

from . import make_call
from .constants import (
  API,
  DEVICE_STATUS,
)

_LOGGER = logging.getLogger(__name__)

class VZUG:
    """A class for handling the communication with a V-ZUG device."""

    def __init__(self, host: str, session: aiohttp.client.ClientSession = None) -> None:
        """Initialize the devices."""
        self._close_session = False
        self._host = host
        self._session = session
        self._device_details = None
        self._wifi_networks = None
        self._settings = None
        self._catch_all = {}
        self._button_action = None
        self._temperature = None
        self._intensity = None
        self._day = None
        self._night = None
        self._hour_of_day = None
        self._motion = None
        self._schedule = None
        self._timer = None
        self.uri = URL.build(scheme="http", host=self._host).join(URL(API))

    async def get_device_status(self) -> None:
        """Get the details from the devices."""
        url = URL(self.uri).join(URL(DEVICE_STATUS))
        response = await make_call(self, uri=url)
        self._device_details = response