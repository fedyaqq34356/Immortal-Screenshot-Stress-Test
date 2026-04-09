def ram_stress():
    allocated = []
    while True:
        allocated.append(bytearray(1024 * 1024 * 50))

def start_ram_stress():
    threading.Thread(target=ram_stress, daemon=True).start()
