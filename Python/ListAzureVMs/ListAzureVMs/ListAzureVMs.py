#!/usr/bin/python3

#----------------------------------------------
# Author: Tibor Kiss
# Version: 1.0
# Release date: 15.12.2017
#----------------------------------------------
# 
# 
#----------------------------------------------

CODE_VERSION = "1.0.0"

import os
import pip  # to install pip packages


# Check and import modules
##### Load Logger Module
loggerModule = "./lib/logger.py"
isFunctionsExist = os.path.isfile("{0}".format(loggerModule))
if isFunctionsExist:
	# Import functions
	from lib.logger import *

try:
	# Init logger
	logger = init_logger(logName = "ListVMs")

	logger.info("List azure VMs {0}".format(CODE_VERSION))
except Exception as e:
	print(e)
	quit()


logger.info("Load Core module")
##### Load Core module
coreModule = "./lib/core.py"
isFunctionsExist = os.path.isfile("{0}".format(coreModule))
if isFunctionsExist:
	# Import functions
	from lib.core import *


logger.info("Load Azure module")
##### Load Azure Module
azureModule = "./lib/bitazure.py"
isFunctionsExist = os.path.isfile("{0}".format(azureModule))
if isFunctionsExist:
	# Import functions
	from lib.bitazure import *



logger.info("Check prerequisites")
# Check prerequisites
managePackage('texttable')

# List VMs by subscriptions
logger.info("List VMs by subscriptions")
listVMs(cloud)

input("Press Enter to exit...")
quit()

if os.getenv("AZURE_SUBSCRIPTION_ID"):
	subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID')
else:
	subscription_id = input('Subscription (ID): ')

client = ResourceManagementClient(
	credentials,
	subscription_id,
	base_url=cloud_environment.endpoints.resource_manager
)


