from loguru import logger
import os
import sys

LOG_FILE = "langchain-translation.log"
ROTATION_TIME = "02:00"

class Logger:
    def __init__(self, name="translation", log_dir="logs", debug=False):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file_path = os.path.join(log_dir, LOG_FILE)
        logger.remove()
        level = "DEBUG" if debug else "INFO"
        logger.add(sys.stdout, level=level)
        logger.add(log_file_path, rotation=ROTATION_TIME, level="DEBUG")
        self.logger = logger
LOG = Logger(debug=True).logger