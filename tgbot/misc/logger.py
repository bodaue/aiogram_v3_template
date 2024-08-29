import logging

import betterlogging

logger = logging.getLogger(__name__)
log_level = logging.INFO
betterlogging.basic_colorized_config(level=log_level)


def setup_logger() -> None:
    logging.basicConfig(
        format="%(filename)s [LINE:%(lineno)d] "
        "#%(levelname)-6s [%(asctime)s]  %(message)s",
        datefmt="%d.%m.%Y %H:%M:%S",
        level=log_level,
    )
    logger.info("Starting bot")
