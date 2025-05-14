import logging
import os
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")

# Create logger
logger = logging.getLogger("word_api_logger")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# File Handler with rotation (1 MB per file, keep 3 backups)
file_handler = RotatingFileHandler(
    LOG_FILE_PATH, maxBytes=1_000_000, backupCount=3
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Add handlers to logger (avoid duplicates)
if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
