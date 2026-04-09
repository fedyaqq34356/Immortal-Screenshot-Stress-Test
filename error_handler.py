import threading

def safe_run(func):
    def wrapper():
        try:
            func()
        except Exception:
            pass
    return wrapper
