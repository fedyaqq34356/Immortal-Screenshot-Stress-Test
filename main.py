import threading
import tkinter as tk
from tkinter import filedialog, messagebox

import screenshot as scr
from stress_cpu import start_cpu_stress
from stress_ram import start_ram_stress
from error_handler import safe_run


def choose_folders():
    root = tk.Tk()
    root.withdraw()

    folders = []
    while True:
        folder = filedialog.askdirectory(title="Select a folder (Cancel when done)")
        if not folder:
            break
        if folder not in folders:
            folders.append(folder)

    root.destroy()
    return folders


def main():
    folders = choose_folders()

    if not folders:
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("No folders selected", "No folders were selected.\nThe program will now exit.")
        root.destroy()
        return

    scr.SELECTED_DIRS.extend(folders)

    threading.Thread(target=safe_run(scr.start_scheduler), daemon=True).start()
    threading.Thread(target=safe_run(start_cpu_stress), daemon=True).start()
    threading.Thread(target=safe_run(start_ram_stress), daemon=True).start()

    threading.Event().wait()


if __name__ == "__main__":
    main()