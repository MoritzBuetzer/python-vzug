"""Exceptions for V-ZUG API client."""

class VZUGError(Exception):
    """General VZUG exception occurred."""
    pass

class VZUGConnectionError(VZUGError):
    """When a connection error is encountered."""
    pass

class VZUGNoDataAvailable(VZUGError):
    """When no data is available."""
    pass