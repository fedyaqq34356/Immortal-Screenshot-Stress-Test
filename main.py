import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os

from screenshot import SELECTED_DIRS, capture_and_save
from stress_cpu import start_cpu_stress
from stress_ram import start_ram_stress
from error_handler import safe_run

def choose_folders():
    global SELECTED_DIRS
    root = tk.Tk()
    root.withdraw()

    while True:
        folder = filedialog.askdirectory(title="Select folder (Cancel to finish selection)")
        if not folder:
            break
        if folder not in SELECTED_DIRS:
            SELECTED_DIRS.append(folder)

    if SELECTED_DIRS:
        messagebox.showinfo("Program Launch",
                          f"Folders selected: {len(SELECTED_DIRS)}\n"
                          f"Screenshot interval: 30 seconds\n\n"
                          f"Program started successfully.\n"
                          f"Screenshots saved with timestamp (2026-04-09_12-30-01.png)")
        
        threading.Thread(target=safe_run(capture_and_save), daemon=True).start()
        threading.Thread(target=safe_run(start_cpu_stress), daemon=True).start()
        threading.Thread(target=safe_run(start_ram_stress), daemon=True).start()
        
    else:
        messagebox.showwarning("Error", "No folders selected.\nProgram will be closed.")

if __name__ == "__main__":
    choose_folders()
    while True:
        time.sleep(10)
