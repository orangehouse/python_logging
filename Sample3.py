# -*- coding: utf-8 -*-

import MyFunc
import logging
logger_name = "LOG"
log_format = '%(asctime)s,%(filename)s,%(funcName)s,%(lineno)d,%(process)d,%(thread)d,%(levelname)s,%(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
log_title = 'Time,FileName,FunctionName,LineNumber,ProcessID,ThreadID,LogLevel,Message\n'

# import datetime
# logFileName = "{0:%Y%m%d%H%M%S}.log".format(datetime.datetime.now())
logFileName = "Sample.log"

logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

handler_format = logging.Formatter(fmt=log_format,
                                   datefmt=date_format)

Stream_handler = logging.StreamHandler()
Stream_handler.setLevel(logging.ERROR)
Stream_handler.setFormatter(fmt=handler_format)

File_handler = logging.FileHandler(logFileName)
File_handler.setLevel(logging.DEBUG)
File_handler.setFormatter(fmt=handler_format)

logger.addHandler(Stream_handler)
logger.addHandler(File_handler)


def main():
    with open(logFileName, "w") as f:
        f.write(log_title)
    logger.info("MAIN_Started")
    MyFunc.MyFunc()
    logger.info("MAIN_Finished")


if __name__ == "__main__":
    main()
