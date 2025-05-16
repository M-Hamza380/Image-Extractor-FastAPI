import logging
import os
import sys
from datetime import datetime
from pathlib import Path

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def ensure_dir_exists(dir_path):
    try:
        dir_path = Path(dir_path)
        if not dir_path.exists():
            os.makedirs(dir_path, exist_ok=True)
        return dir_path
    except Exception as e:
        print(f"Error in ensure_dir_exists function: {e}")
        return None


# Logs directory
BASE_DIR = Path(__file__).parent.parent.parent
log_dir = BASE_DIR / "logs"

# Current day and create directory
current_dir = datetime.now().strftime("%A")
day_dir = os.path.join(log_dir, current_dir)
ensure_dir_exists(day_dir)


def directory_with_timestamp(base_time):
    try:
        timestamp = base_time.strftime("%d-%m-%Y_%H-%M")
        timestamp_dir = os.path.join(day_dir, timestamp)
        ensure_dir_exists(timestamp_dir)
        return timestamp_dir
    except Exception as e:
        print(f"Error in directory_with_timestamp function: {e}")
        return None


base_time = datetime.now()
timestamp_dir = directory_with_timestamp(base_time)
if timestamp_dir is None:
    raise RuntimeError(
        "Failed to create or access the timestamp directory for logging."
    )

log_file_paths = {
    logging.INFO: os.path.join(timestamp_dir, "info.log"),
    logging.DEBUG: os.path.join(timestamp_dir, "debug.log"),
    logging.WARNING: os.path.join(timestamp_dir, "warning.log"),
    logging.CRITICAL: os.path.join(timestamp_dir, "critical.log"),
    logging.ERROR: os.path.join(timestamp_dir, "error.log"),
}

logs_format = "[ [%(asctime)s] : %(levelname)s : %(name)s : %(pathname)s : %(module)s : %(lineno)d : %(message)s ]"

logger = logging.getLogger("MID_AI_APIs")
logger.setLevel(logging.DEBUG)
logger.propagate = False


# LevelFilter to allow only specific log levels
class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


# File handler for each log level
def create_file_handler(level, log_file_path):
    try:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.addFilter(LevelFilter(level))
        file_handler.setFormatter(logging.Formatter(logs_format))
        return file_handler
    except Exception as e:
        print(f"Error in create_file_handler function: {e}")
        raise e


# Add file handlers to the logger
for level, log_filepath in log_file_paths.items():
    handler = create_file_handler(level, log_filepath)
    logger.addHandler(handler)


# Function to return color for log levels
def get_color_for_level(level):
    try:
        if level == logging.DEBUG:
            return Fore.CYAN
        elif level == logging.INFO:
            return Fore.GREEN
        elif level == logging.WARNING:
            return Fore.YELLOW
        elif level == logging.ERROR:
            return Fore.RED
        elif level == logging.CRITICAL:
            return Fore.MAGENTA
        return Fore.WHITE
    except Exception as e:
        print(f"Error in get_color_for_level function: {e}")
        raise e


# Console Handler for colored output
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)


# Custom Formatter for color-coding the console output
class ColorFormatter(logging.Formatter):
    def format(self, record):
        try:
            log_message = super().format(record)
            color = get_color_for_level(record.levelno)
            return color + log_message + Style.RESET_ALL
        except Exception as e:
            print(f"Error in ColorFormatter function: {e}")
            raise e


# Set up console handler with color formatter
console_handler.setFormatter(ColorFormatter(logs_format))
logger.addHandler(console_handler)
