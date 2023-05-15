import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent

LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'log.log'
IMAGES_DIR = BASE_DIR / 'images'

TELEGRAM_USER_ID = os.getenv('TELEGRAM_USER_ID')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendVideo'

IMAGES_MINUTES_INTERVAL = 15
TIMELAPSE_CREATE_TIME = "23:50"
TIMELAPSE_SEND_TIME = "16:55"
DELETE_FILES_TIME = "16:58"

ANNOTATE_FORMAT = "%d.%m.%Y %H:%M"
IMAGE_FILE_NAME = "%d.%m.%Y %H:%M.jpg"
TIMELAPSE_FILE_NAME = 'timelapse.mp4'