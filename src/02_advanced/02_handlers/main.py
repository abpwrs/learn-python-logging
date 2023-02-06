import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import time

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)-10s | %(message)s"
)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)


console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("02_advanced_02_file_handler.log")
rotating_file_handler = RotatingFileHandler(
    "02_advanced_02_rotating.log", maxBytes=2000, backupCount=5
)
timed_rotating_file_handler = TimedRotatingFileHandler(
    "02_advanced_02_timed_rotating.log", when="s", interval=30, backupCount=5
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
rotating_file_handler.setFormatter(formatter)
timed_rotating_file_handler.setFormatter(formatter)

root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)
root_logger.addHandler(rotating_file_handler)
root_logger.addHandler(timed_rotating_file_handler)

i = 0
while True:
    root_logger.info(f"hi there. i={i}")
    time.sleep(2)
    i += 1
