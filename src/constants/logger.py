import logging

# Default log level if environment variable is not set or has an invalid value
default_log_level = logging.ERROR

# Map log level names to their corresponding logging constants
log_level_mapping = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}
