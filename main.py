import os
import time
from datetime import datetime
import mss
from PIL import Image
import schedule
import threading

SELECTED_DIRS = []
INTERVAL_SECONDS = 30

def get_daily_folder(base_dir):
    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join(base_dir, today)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def get_timestamp_path(folder, extension=".png"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(folder, f"{timestamp}{extension}")

def capture_and_save():
    if not SELECTED_DIRS:
        return
    for base_dir in SELECTED_DIRS:
        try:
            daily_folder = get_daily_folder(base_dir)
            png_path = get_timestamp_path(daily_folder, ".png")
            txt_path = get_timestamp_path(daily_folder, ".txt")
            with mss.mss() as sct:
                screenshot = sct.shot(mon=-1)
                img = Image.open(screenshot)
            img.save(png_path)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("immortal")
        except:
            pass

def start_scheduler():
    schedule.every(INTERVAL_SECONDS).seconds.do(capture_and_save)
    while True:
        schedule.run_pending()
        time.sleep(1)
