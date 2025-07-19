import os
import socket
import logging
import logstash
from datetime import datetime
from settings import (
    LOGSTASH_ENABLED, 
    LOGSTASH_HOST, 
    LOGSTASH_PORT
)

import logging

def regular_logging():
    class CustomFormatter(logging.Formatter):
        def format(self, record):
            extra_msg = " ".join(
                f"{key}={value}" 
                for key, value in record.__dict__.items() 
                if key not in [
                    "msg", "args", "levelname", "levelno", "pathname", "filename", "module",
                    "exc_info", "exc_text", "stack_info", "lineno", "funcName", "created", 
                    "msecs", "relativeCreated", "thread", "threadName", "processName", 
                    "process", "message", "asctime", "correlation_id"
                ]
            )
            if extra_msg:
                return f"{super().format(record)} ({extra_msg})"
            return super().format(record)
    formatter = CustomFormatter("%(asctime)s [%(levelname)s] (%(correlation_id)s) %(message)s")
    handlers = [
                logging.FileHandler("debug.log"),
                logging.StreamHandler()
            ]
    for handler in handlers:
        handler.setFormatter(formatter)

    logging.basicConfig(
        level=logging.INFO,
        force=True,
        handlers=handlers
    )

def test_logstash_connection():
    """Test if we can connect to Logstash"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((LOGSTASH_HOST, LOGSTASH_PORT))
        sock.close()
        if result == 0:
            print(f"✅ Successfully connected to Logstash at {LOGSTASH_HOST}:{LOGSTASH_PORT}")
            return True
        else:
            print(f"❌ Cannot connect to Logstash at {LOGSTASH_HOST}:{LOGSTASH_PORT}")
            return False
    except Exception as e:
        print(f"❌ Error connecting to Logstash: {e}")
        return False

def setup_logging_logstash():
    # Test connection first
    if not test_logstash_connection():
        print("Using console logging as fallback")
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] (%(correlation_id)s) %(message)s",
        )
        return
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    
    try:
        # Add Logstash handler with additional fields
        logstash_handler = logstash.TCPLogstashHandler(
            host=LOGSTASH_HOST,
            port=LOGSTASH_PORT,
            version=1,
            message_type='Application Log',
            fqdn=False,
            tags=['bedrock-access-gateway']
        )
        
        logger.addHandler(logstash_handler)
        
        # Test logging
        logging.info("Logstash handler configured successfully", extra={
            'startup_time': datetime.now().isoformat()
        })
        
    except Exception as e:
        print(f"Failed to setup Logstash handler: {e}, falling back to console")
        # Fallback to console
        regular_logging()

def setup_logging():
    if LOGSTASH_ENABLED:
        setup_logging_logstash()
    else:
        regular_logging()