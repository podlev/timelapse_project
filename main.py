import logging
import time

import ffmpeg
import requests
import schedule

from camera import camera
from config import configure_logging
from settings import (
    IMAGES_MINUTES_INTERVAL,
    TIMELAPSE_CREATE_TIME,
    TELEGRAM_URL,
    TELEGRAM_USER_ID, TIMELAPSE_SEND_TIME, DELETE_FILES_TIME
)
from utils import (
    delete_files_and_directory,
    get_image_file,
    get_annotate_text,
    get_timelapse_file, get_current_directory
)


def send_timelapse():
    timelapse_file = get_timelapse_file().as_posix()
    try:
        with open(timelapse_file, 'rb') as video:
            files = {'video': video}
            params = {'chat_id': TELEGRAM_USER_ID}
            response = requests.post(TELEGRAM_URL, params=params, files=files)
            if response.status_code == 200:
                logging.info(f'Timelapse send successfully: {timelapse_file}')
            else:
                logging.error(f'Timelapse send error: {response.status_code}')
    except FileNotFoundError:
        logging.error(f'Timelapse open error: {timelapse_file}')
        return
    except requests.exceptions.RequestException as e:
        logging.error(f'Error while sent video: {e}')


def create_image():
    image_file = get_image_file().as_posix()
    try:
        camera.annotate_text = get_annotate_text()
        camera.capture(image_file)
        logging.info(f'Create image success: {image_file}')
    except Exception as e:
        logging.error(f'Create image error: {e}')


def create_timelapse(file=None, directory=None):
    timelapse_file = file or get_timelapse_file().as_posix()
    current_directory = directory or get_current_directory().as_posix()
    try:
        (
            ffmpeg
            .input(f'{current_directory}/*.jpg', pattern_type='glob', framerate=5)
            .output(timelapse_file, crf=20, pix_fmt='yuv420p')
            .global_args('-loglevel', 'error')
            .run()
        )
        logging.info(f'Create timelapse success: {timelapse_file}')
    except Exception as e:
        logging.error(f'Create timelapse error: {e}')


if __name__ == '__main__':
    configure_logging()
    logging.info('Start timelapse project')

    schedule.every(IMAGES_MINUTES_INTERVAL).minutes.do(create_image)
    schedule.every().day.at(TIMELAPSE_CREATE_TIME).do(create_timelapse)
    schedule.every().day.at(TIMELAPSE_SEND_TIME).do(send_timelapse)
    schedule.every().day.at(DELETE_FILES_TIME).do(delete_files_and_directory)

    while True:
        schedule.run_pending()
        time.sleep(1)
