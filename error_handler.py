import logging

logging.basicConfig(
    filename="immortal_errors.log",
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def safe_run(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}", exc_info=True)
    return wrapper