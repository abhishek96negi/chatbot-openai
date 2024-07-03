from src.constants.env_constant import env_var
from src.constants.logger import (
    default_log_level,
    log_level_mapping
)
import logging
import sys


# Determine the log level based on the environment variable
log_level = log_level_mapping.get(env_var.get("LOG_LEVEL"), default_log_level)

# Configure the logging settings
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s [%(filename)s:%(lineno)s - %(funcName)s ] - %(message)s",
    level=log_level,
    stream=sys.stdout,  # directing logs to the standard output
)
