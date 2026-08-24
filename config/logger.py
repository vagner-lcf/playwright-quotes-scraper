import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("execution.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )