import logging

from logging import config


config.dictConfig(
    {
        "version": 1,
        "filters": {},
        "formatters": {
            "detailed": {
                "class": "logging.Formatter",
                "format": "%(asctime)s | %(levelname)-8s | %(name)s | %(threadName)s:%(thread)d | %(message)s",
            },
            "minimal": {
                "class": "logging.Formatter",
                "format": "%(asctime)s | %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "filters": [],
                "formatter": "detailed",
            },
            "main_file": {
                "class": "logging.FileHandler",
                "filename": "02_advanced_05.log",
                "filters": [],
                "formatter": "minimal",
            },
        },
        "root": {
            "level": "ERROR",
            "handlers": ["console"],
        },
        "loggers": {
            "example": {
                "level": "INFO",
                "handlers": ["main_file"],
            },
        },
    }
)

logging.critical("hello")
logging.error("world")
logging.getLogger("example").error("error to the file")
logging.getLogger("example").info("info to the file")
logging.getLogger("example").debug("debug goes nowhere")
