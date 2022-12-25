import logging
import os
from datetime import datetime
from Utility.app_configs import Configs as cfg


def log(level, msg):
    date = datetime.now().strftime("%Y%m%d")
    # checking if the logs directory Exists
    # if not create one.
    if not os.path.isdir(cfg().logsDir):
        os.makedirs(cfg().logsDir)

    logging.basicConfig(filemode='a', filename=cfg().logsDir + str(date) + '.log',
                        format='%(asctime)s - %(levelname)s -  %(message)s')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

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
