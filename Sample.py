# -*- coding: utf-8 -*-

import logging
# import datetime
# logFileName = "{0:%Y%m%d%H%M%S}.log".format(datetime.datetime.now())
logFileName = "Sample.log"
logging.basicConfig(filename=logFileName,
                    format='%(asctime)s,%(levelname)s,%(funcName)s,%(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    level=logging.DEBUG)


def main():
    logging.debug("debug")          # 10
    logging.info("info")            # 20
    logging.warning("warning")      # 30
    logging.error("error")          # 40
    logging.critical("critical")    # 50


if __name__ == "__main__":
    logging.info("Started")
    main()
    logging.info("Finished")
