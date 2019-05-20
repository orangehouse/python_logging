# -*- coding: utf-8 -*-

import logging
log_format = '%(asctime)s,%(filename)s,%(funcName)s,%(process)d,%(levelname)s,%(message)s'
date_format = '%Y-%m-%d %H:%M:%S'

# import datetime
# logFileName = "{0:%Y%m%d%I%M%S}.log".format(datetime.datetime.now())
logFileName = "Sample.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler_format = logging.Formatter(fmt=log_format,
                                   datefmt=date_format)

Stream_handler = logging.StreamHandler()
Stream_handler.setLevel(logging.DEBUG)
Stream_handler.setFormatter(fmt=handler_format)

File_handler = logging.FileHandler(logFileName)
File_handler.setLevel(logging.DEBUG)
File_handler.setFormatter(fmt=handler_format)

logger.addHandler(Stream_handler)
logger.addHandler(File_handler)

def sub():
    logger.debug("Hello world!")


if __name__ == "__main__":
    logger.info("Started")
    sub()
    logger.info("Finished")
