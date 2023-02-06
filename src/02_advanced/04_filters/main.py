import logging

from typing import Optional


class TextContentFilter(logging.Filter):
    def __init__(self, param: Optional[str] = None):
        self.param = param

    def filter(self, record: logging.LogRecord):
        if self.param is None:
            allow = True
        else:
            allow = self.param not in record.msg
        return allow


class LevelFilter(logging.Filter):
    def __init__(self, level: Optional[int]):
        self.level = level

    def filter(self, record: logging.LogRecord):
        if self.level is not None and record.levelno == self.level:
            return False

        return True


root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()

console_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(threadName)s:%(thread)d | %(message)s"
    )
)
root_logger.addHandler(console_handler)
root_logger.addFilter(TextContentFilter("noshow"))
root_logger.addFilter(TextContentFilter("dont show this"))
root_logger.addFilter(LevelFilter(logging.WARNING))


root_logger.debug("hello")
root_logger.debug("hello - noshow")
root_logger.debug("show this")
root_logger.debug("dont show this")

root_logger.debug("debug is okay")
root_logger.info("info is okay")
root_logger.warning("warning is not okay")
root_logger.error("error is okay")
root_logger.critical("critical is okay")
