import os
import time
from datetime import datetime

import mss
from PIL import Image
import schedule

SELECTED_DIRS = []
INTERVAL_SECONDS = 30


def get_daily_folder(base_dir):
    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join(base_dir, today)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def capture_and_save():
    if not SELECTED_DIRS:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    with mss.mss() as sct:
        monitor = sct.monitors[0]
        raw = sct.grab(monitor)
        img = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")

    for base_dir in SELECTED_DIRS:
        try:
            daily_folder = get_daily_folder(base_dir)
            png_path = os.path.join(daily_folder, f"{timestamp}.png")
            txt_path = os.path.join(daily_folder, f"{timestamp}.txt")

            img.save(png_path)

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("immortal")
        except Exception:
            pass


def start_scheduler():
    capture_and_save()

    schedule.every(INTERVAL_SECONDS).seconds.do(capture_and_save)

    while True:
        schedule.run_pending()
        time.sleep(1)