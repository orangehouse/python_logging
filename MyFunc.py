# -*- coding: utf-8 -*-

import logging
logger_name = "LOG"
logger = logging.getLogger(logger_name)

def sub():
    print("TEST2")

def MyFunc():
    logger.info("Started")
    sub()
    logger.info("Finished")