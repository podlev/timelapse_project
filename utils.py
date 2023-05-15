import logging
import shutil
from datetime import datetime

from settings import IMAGES_DIR, ANNOTATE_FORMAT, IMAGE_FILE_NAME, TIMELAPSE_FILE_NAME


def get_current_directory():
    IMAGES_DIR.mkdir(exist_ok=True)
    current_directory = IMAGES_DIR / datetime.now().strftime('%d')
    current_directory.mkdir(exist_ok=True)
    return current_directory


def get_image_file():
    return get_current_directory() / datetime.now().strftime(IMAGE_FILE_NAME)


def get_annotate_text():
    return datetime.now().strftime(ANNOTATE_FORMAT)


def get_timelapse_file():
    return get_current_directory() / TIMELAPSE_FILE_NAME


def delete_files_and_directory():
    directory = get_current_directory()
    logging.info(f'Delete files and directory: {directory}')
    shutil.rmtree(directory)
