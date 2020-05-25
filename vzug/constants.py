"""Constants used by the Python API for interacting with V-ZUG devices."""
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("setuptools").version
except Exception:
    __version__ = "unknown"

TIMEOUT = 10

USER_AGENT = f"PythonVZUG/{__version__}"
API = "/ai"

DEVICE_STATUS = "getDeviceStatus"

# Communication constants
CONTENT_TYPE_JSON = "application/json"
CONTENT_TYPE = 'Content-Type'
CONTENT_TYPE_TEXT_PLAIN = "text/plain"