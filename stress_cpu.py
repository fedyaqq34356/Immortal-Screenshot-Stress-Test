import os
import threading


def _cpu_worker():
    while True:
        _ = sum(i * i for i in range(100_000))


def start_cpu_stress():
    num_cores = os.cpu_count() or 4
    for _ in range(num_cores):
        t = threading.Thread(target=_cpu_worker, daemon=True)
        t.start()