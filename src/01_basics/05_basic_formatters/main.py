import logging

logging.basicConfig(
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    filename="01_basics_05.log",
    encoding="utf-8",
    level=logging.DEBUG,
)
logging.debug("Some very specific information")
logging.info("Noting to worry about here")
logging.warning("Do you smell something burning")
logging.error("Ope, yup that is definitely on fire")
logging.critical("Run for your lives")
