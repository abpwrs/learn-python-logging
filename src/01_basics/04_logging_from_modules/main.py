import logging
import module_a


def main():
    logging.basicConfig(
        filename="01_basics_04.log", encoding="utf-8", level=logging.DEBUG
    )

    logging.debug("Hello, World!")
    logging.info("Hello, World!")
    module_a.do_something()
    logging.warning("Hello, World!")
    logging.error("Hello, World!")
    logging.critical("Hello, World!")


if __name__ == "__main__":
    main()
