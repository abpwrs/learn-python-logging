import logging

fmt_str = "%(asctime)s | %(levelname)-8s | %(name)-10s | %(message)s"
# root logging config
logging.basicConfig(
    format=fmt_str,
    encoding="utf-8",
    level=logging.WARNING,
)

# build an arbitrary namespace hierarchy w/ different levels and loggers
a_logger = logging.getLogger("a")
a_logger.info("I inherit the root logging level -- this won't print to console")
a_logger.warning("I inherit the root logging level -- this will print to console")

a_b_logger = logging.getLogger("a.b")
a_b_logger.setLevel(logging.DEBUG)
a_b_logger.info("I've been manually set to DEBUG -- so you can see this message")
a_b_logger.debug("this one too!")

a_b_one_logger = logging.getLogger("a.b.1")
a_b_one_logger.setLevel(logging.CRITICAL)
a_b_one_logger.warning("I've been set to a very high level, you won't see this")
a_b_one_logger.error("won't see this either")
a_b_one_logger.critical("I've been set to a very high level -- you will see this")

a_b_two_logger = logging.getLogger("a.b.2")
a_b_two_logger.info("I inherit from a.b -- so you can see this!!")

a_c_logger = logging.getLogger("a.c")
a_c_file_handler = logging.FileHandler("02_advanced_01_a_c.log")
a_c_file_handler.setFormatter(logging.Formatter(fmt_str))
a_c_logger.addHandler(a_c_file_handler)

a_c_logger.info("I inherit from 'a' -- you won't see this")
a_c_logger.warning(
    "I inherit from 'a' -- you will see this! will also be in 02_advanced_01_a_c.log"
)

a_c_one_logger = logging.getLogger("a.c.1")
a_c_one_logger.setLevel(logging.INFO)
a_c_one_logger.debug("I won't log to console, or to 02_advanced_01_a_c.log")
a_c_one_logger.info("I will log to console, and to 02_advanced_01_a_c.log")
