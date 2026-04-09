import os

def cpu_stress():
    while True:
        _ = sum(i * i for i in range(100000))

def start_cpu_stress():
    num_cores = os.cpu_count() or 4
    for _ in range(num_cores):
        threading.Thread(target=cpu_stress, daemon=True).start()
