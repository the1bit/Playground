
#!/usr/bin/python3

#----------------------------------------------
# Author: Tibor Kiss
# Version: 1.0
# Release date: 15.12.2017
#----------------------------------------------
# Logger module for Python 3
# collection of logger functions for python.
#----------------------------------------------

import logging
import os
import os.path
import time

###### Initialize logging #########
def init_logger(logName = "logpy", logPath = "./log", logLevel = "INFO"):
	timestr = time.strftime("%Y%m%d-%H%M%S")

	logFilename = "{0}/{1}-{2}.log".format(logPath, logName, timestr)

	if not os.path.exists(logPath):
		os.makedirs(logPath)

	global logger
	logger = logging.getLogger(logName)

	# File logger
	hdlr = logging.FileHandler(logFilename)
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr)

	# Screen logger
	consoleHandler = logging.StreamHandler()
	consoleHandler.setFormatter(formatter)
	logger.addHandler(consoleHandler)


	# Set log level
	if logLevel.lower() == "critical":
		logger.setLevel(logging.CRITICAL)
	elif logLevel.lower() == "error":
		logger.setLevel(logging.ERROR)
	elif logLevel.lower() == "warning":
		logger.setLevel(logging.WARNING)
	elif logLevel.lower() == "info":
		logger.setLevel(logging.INFO)
	elif logLevel.lower() == "debug":
		logger.setLevel(logging.DEBUG)
	else:
		logger.setLevel(logging.NOTSET)
	
	return logger

###### End of Initialize logging #########
