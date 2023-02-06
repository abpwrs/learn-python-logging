import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()

root_logger.addHandler(console_handler)


def update_format(fmt_str: str):
    console_handler.setFormatter(logging.Formatter(fmt_str, "%Y-%m-%d %H:%M:%S"))


def log_w_format(fmt_str: str):
    update_format(fmt_str)
    root_logger.info(f"{fmt_str}")
    root_logger.critical(f"{fmt_str}")


log_w_format("%(message)s")
log_w_format("%(asctime)s | %(message)s")
log_w_format("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")
log_w_format(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(threadName)s:%(thread)d | %(message)s"
)
log_w_format(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(threadName)s:%(thread)d | %(module)s | %(message)s"
)
log_w_format(
    "%(asctime)s | %(levelname)-8s | %(name)s | pid:%(process)d | thread:%(thread)d | %(pathname)s:%(lineno)d | %(message)s"
)
