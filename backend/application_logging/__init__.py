import logging
from asgi_correlation_id import correlation_id

logger = logging.getLogger(__name__)
def log_message(log_identifier, data, level=logging.INFO):
    message = {
        "identifier": log_identifier,
        "correlation_id": correlation_id.get() or "",
        "data": data
    }
    logger.log(level, log_identifier, extra=message)

def log_exception(log_identifier, exception, level=logging.ERROR):
    log_message(
        log_identifier,
        {"error": str(exception)},
        level
    )