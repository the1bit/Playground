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


#if checkSubscription('a3499378-a5d6-413c-8f88-535b0826ca96', subscription_list):

import datetime;
today = datetime.datetime.now().date();
yesterday = today - datetime.timedelta(days=1);

print("Get All avaiulable Metrics for VMs")
for subsc in subscription_list:
	print("---> Subscription: '{0}' - {1}".format(subsc.display_name, subsc.subscription_id))
	resourcemanager_client = newResourceManagerClient(subsc.subscription_id)
	for group in resourcemanager_client.resource_groups.list():
		print(group.name)
		for item in resourcemanager_client.resources.list_by_resource_group(group.name):
			#if "Microsoft.Compute/virtualMachines" == str(item.type):
				print(item.name)
				monitor_client = newMonitoringClient(subsc.subscription_id)
				listAvailableMetrics(monitor_client, item.id, yesterday, today)
				

	#compute_client = newComputeClient(subsc.subscription_id)
	resourcemanager_client = newResourceManagerClient(subsc.subscription_id)
	#getVMs(subsc.subscription_id, compute_client)


# List VMs by subscriptions
#logger.info("List VMs by subscriptions")
#listVMs(subscription_list) 


# Exit from script !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
input("Press Enter to exit...")
quit()
