import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("What should be logged when:")
logging.debug(
    "Detailed information, typically of interest only when diagnosing problems."
)
logging.info("Confirmation that things are working as expected.")
logging.warning(
    "An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected."
)
logging.error(
    "Due to a more serious problem, the software has not been able to perform some function."
)
logging.critical(
    "A serious error, indicating that the program itself may be unable to continue running."
)
