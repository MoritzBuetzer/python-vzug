"""Constants used by the Python V-ZUG API."""
import pkg_resources
from yarl import URL

try:
    __version__ = pkg_resources.get_distribution("setuptools").version
except Exception:
    __version__ = "unknown"

TIMEOUT = 10

USER_AGENT = f"PythonVZUG/{__version__}"
API = URL("/ai")
API2 = URL("/hh")

DEVICE_STATUS = "getDeviceStatus"
PROGRAM_STATUS = "getProgram"

# Communication constants
CONTENT_TYPE_JSON = "application/json"
CONTENT_TYPE = 'Content-Type'
CONTENT_TYPE_TEXT_PLAIN = "text/plain"