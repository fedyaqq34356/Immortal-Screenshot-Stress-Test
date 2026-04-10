import threading

def ram_stress():
    allocated = []
    while True:
        block = bytearray(1024 * 1024 * 500)
        allocated.append(block)

def start_ram_stress():
    for _ in range(12):
        threading.Thread(target=ram_stress, daemon=True).start()
