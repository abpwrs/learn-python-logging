import logging
from logging import config
from pathlib import Path

conf_file = str(Path(__file__).parent / "logging.conf")

with open(conf_file, "r") as f:
    config.fileConfig(f)

logging.critical("hello")
logging.error("world")
logging.getLogger("example").error("error to the file")
logging.getLogger("example").info("info to the file")
logging.getLogger("example").debug("debug goes nowhere")
