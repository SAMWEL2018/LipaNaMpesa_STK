import logging

logging.basicConfig(filemode='a', filename='/app.log', format='%(asctime)s - %(levelname)s -  %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


def log(level, msg):
    match level:
        case 1:  # INFO
            logger.info(msg)
        case 2:  # ERROR
            logger.error(msg)
        case 3:  # WARNING
            logger.warning(msg)
        case 4:  # DEBUG
            logger.debug(msg)
        case _:
            print("Unknown Error Logging Level")

