import logging

# anything you can put in a string can go in a log
NAME = "World"
# NAME = {"a", "b"}
# NAME = [1, 2, 3]

logging.basicConfig(level=logging.DEBUG)
logging.debug(f"Hello, {NAME}!")
logging.info(f"Hello, {NAME}!")
logging.warning(f"Hello, {NAME}!")
logging.error(f"Hello, {NAME}!")
logging.critical(f"Hello, {NAME}!")
