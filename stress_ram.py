import threading


def _ram_worker():
    allocated = []
    while True:
        allocated.append(bytearray(1024 * 1024 * 50))


def start_ram_stress():
    t = threading.Thread(target=_ram_worker, daemon=True)
    t.start()