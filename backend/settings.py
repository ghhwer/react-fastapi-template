import os

TITLE = "Example of Backend Application"
SUMMARY = "RESTful APIs"
VERSION = "0.1.0"
DESCRIPTION = """
My REST API
"""

API_ROUTE_PREFIX = os.environ.get("API_ROUTE_PREFIX", "/api/v1")
DEBUG = os.environ.get("DEBUG", "false").lower() != "false"

LOGSTASH_ENABLED = os.environ.get("LOGSTASH_ENABLED", "false").lower() != "false"
LOG_DESTINATION = os.getenv("LOG_DESTINATION", "logstash:5044")
LOGSTASH_HOST, LOGSTASH_PORT = LOG_DESTINATION.split(":")
LOGSTASH_PORT = int(LOGSTASH_PORT)