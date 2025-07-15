"""
Logging setup and shared logger for the xpublish_wms package.
"""
import logfire
import logging

# Set up a shared logger for the xpublish_wms package
logging.basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = logging.getLogger("xpublish_wms")
